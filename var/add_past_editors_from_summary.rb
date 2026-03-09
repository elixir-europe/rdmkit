#!/usr/bin/env ruby
# frozen_string_literal: true

require 'yaml'
require 'json'
require 'net/http'
require 'uri'
require 'set'
require 'date'

SUMMARY_PATH = 'summary.md'
CONTRIBUTORS_PATH = '_data/CONTRIBUTORS.yaml'
OWNER = 'elixir-europe'
REPO = 'rdmkit'

PAST_EDITOR_NAMES = [
  'Mijke Jetten',
  'Niclas Jareborg',
  'Pinar Alper',
  'Rob Hooft',
  'Daniel Faria',
  'Martin Cook',
  'Laura Portell Silva'
].freeze

def github_get(path, params, token)
  uri = URI("https://api.github.com/repos/#{OWNER}/#{REPO}#{path}")
  uri.query = URI.encode_www_form(params)

  req = Net::HTTP::Get.new(uri)
  req['Accept'] = 'application/vnd.github+json'
  req['X-GitHub-Api-Version'] = '2022-11-28'
  req['User-Agent'] = 'rdmkit-past-editors-script'
  req['Authorization'] = "Bearer #{token}" if token && !token.empty?

  res = Net::HTTP.start(uri.host, uri.port, use_ssl: true, read_timeout: 30) { |http| http.request(req) }
  unless res.code.to_i.between?(200, 299)
    raise "GitHub API error #{res.code} for #{path}: #{res.body.to_s[0, 200]}"
  end
  JSON.parse(res.body)
end

def github_paginated(path, token)
  out = []
  page = 1
  loop do
    payload = github_get(path, { per_page: 100, page: page }, token)
    raise "Unexpected payload for #{path}" unless payload.is_a?(Array)

    out.concat(payload)
    break if payload.length < 100

    page += 1
  end
  out
end

def participants_for_pr(pr_number, token, cache)
  return cache[pr_number] if cache.key?(pr_number)

  people = Set.new

  reviews = github_paginated("/pulls/#{pr_number}/reviews", token)
  reviews.each do |review|
    user = review.is_a?(Hash) ? review['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    state = review.is_a?(Hash) ? review['state'].to_s.upcase : ''
    people << login if !login.empty? && %w[APPROVED COMMENTED CHANGES_REQUESTED].include?(state)
  end

  issue_comments = github_paginated("/issues/#{pr_number}/comments", token)
  issue_comments.each do |comment|
    user = comment.is_a?(Hash) ? comment['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    people << login unless login.empty?
  end

  pr_comments = github_paginated("/pulls/#{pr_number}/comments", token)
  pr_comments.each do |comment|
    user = comment.is_a?(Hash) ? comment['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    people << login unless login.empty?
  end

  cache[pr_number] = people
  people
end

def split_editors(text)
  return [] if text.to_s.strip.empty?
  text.split(',').map(&:strip).reject(&:empty?)
end

def unique_preserve_order(values)
  seen = Set.new
  out = []
  values.each do |v|
    next if v.to_s.strip.empty?
    next if seen.include?(v)

    seen << v
    out << v
  end
  out
end

def split_front_matter(content)
  lines = content.lines
  return [nil, nil, nil] unless lines[0]&.strip == '---'

  end_idx = nil
  lines.each_with_index do |line, idx|
    next if idx.zero?
    if line.strip == '---'
      end_idx = idx
      break
    end
  end
  return [nil, nil, nil] if end_idx.nil?

  [lines[0..0], lines[1...end_idx], lines[end_idx..]]
end

def read_front_matter(path)
  content = File.read(path, encoding: 'UTF-8')
  _s, middle, _t = split_front_matter(content)
  return {} if middle.nil?
  YAML.safe_load(middle.join, permitted_classes: [Date, Time], aliases: true) || {}
rescue
  {}
end

def render_editors_line(editors)
  "editors: [#{editors.join(', ')}]\n"
end

def update_editors_line(path, editors)
  content = File.read(path, encoding: 'UTF-8')
  start, middle, tail = split_front_matter(content)
  return false if middle.nil?

  new_line = render_editors_line(editors)
  updated = []
  found = false

  middle.each do |line|
    if line.match?(/^editors:\s*/)
      updated << new_line unless found
      found = true
    else
      updated << line
    end
  end

  unless found
    insert_at = updated.length
    idx = updated.find_index { |line| line.match?(/^contributors:\s*/) }
    insert_at = idx + 1 unless idx.nil?
    updated.insert(insert_at, new_line)
  end

  new_content = (start + updated + tail).join
  return false if new_content == content

  File.write(path, new_content, mode: 'w', encoding: 'UTF-8')
  true
end

def unwrap_markdown_link(text)
  m = text.to_s.strip.match(/^\[(.+?)\]\((.+)\)$/)
  return [m[1], m[2]] if m

  [text.to_s.strip, nil]
end

token = ENV['GH_TOKEN'] || ENV['GITHUB_TOKEN']
contributors = YAML.safe_load(File.read(CONTRIBUTORS_PATH, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}

# name -> login, constrained to requested past editors only
past_editor_login_by_name = {}
PAST_EDITOR_NAMES.each do |name|
  meta = contributors[name]
  next unless meta.is_a?(Hash)

  git = meta['git'].to_s.strip.downcase
  next if git.empty?

  past_editor_login_by_name[name] = git
end

if past_editor_login_by_name.empty?
  abort('None of the requested past editors have git IDs in CONTRIBUTORS.')
end

lines = File.readlines(SUMMARY_PATH, chomp: true)
header_end = lines.index { |l| l.start_with?('|---') }
abort('Could not find markdown table header in summary.md') if header_end.nil?

prefix_lines = lines[0...header_end - 1]
rows = []
lines[(header_end + 1)..-1].to_a.each do |line|
  next unless line.start_with?('|')
  cols = line.sub(/\A\|/, '').sub(/\|\s*\z/, '').split('|').map(&:strip)
  next if cols.length < 3

  page_col, pr_col, editors_col = cols[0], cols[1], cols[2]
  page_label, _page_url = unwrap_markdown_link(page_col)
  _pr_label, pr_url = unwrap_markdown_link(pr_col)

  pr_number = nil
  if pr_url && (m = pr_url.match(%r{/pull/(\d+)}))
    pr_number = m[1].to_i
  elsif (m = pr_col.match(/#(\d+)/))
    pr_number = m[1].to_i
  end

  rows << {
    page_label: page_label,
    page_col: page_col,
    pr_col: pr_col,
    pr_number: pr_number,
    editors: split_editors(editors_col)
  }
end

participants_cache = {}
page_additions = Hash.new { |h, k| h[k] = [] }
updated_rows = []

rows.each do |row|
  additions = []
  if row[:pr_number]
    participants = participants_for_pr(row[:pr_number], token, participants_cache)
    PAST_EDITOR_NAMES.each do |name|
      login = past_editor_login_by_name[name]
      next unless login
      additions << name if participants.include?(login)
    end
  end

  merged = unique_preserve_order(row[:editors] + additions)
  page_additions[row[:page_label]].concat(additions)

  updated_rows << row.merge(editors: merged)
end

# Update page front matter
files_changed = 0
page_additions.each do |page_path, adds|
  next if adds.empty?
  next unless File.exist?(page_path)

  fm = read_front_matter(page_path)
  existing = fm['editors']
  existing_list = if existing.is_a?(Array)
                    existing
                  elsif existing.is_a?(String) && !existing.strip.empty?
                    [existing.strip]
                  else
                    []
                  end

  merged = unique_preserve_order(existing_list + adds)
  files_changed += 1 if update_editors_line(page_path, merged)
end

# Rebuild table
new_lines = []
new_lines.concat(prefix_lines)
new_lines << '| Page | Chosen PR | Editors |'
new_lines << '|---|---:|---|'
updated_rows.each do |row|
  editors_text = row[:editors].join(', ')
  new_lines << "| #{row[:page_col]} | #{row[:pr_col]} | #{editors_text} |"
end

File.write(SUMMARY_PATH, new_lines.join("\n") + "\n", mode: 'w', encoding: 'UTF-8')

puts "Updated summary rows: #{updated_rows.length}"
puts "Page files changed: #{files_changed}"
puts "Past editors considered: #{past_editor_login_by_name.keys.join(', ')}"
