#!/usr/bin/env ruby
# frozen_string_literal: true

require 'yaml'
require 'json'
require 'net/http'
require 'uri'
require 'optparse'
require 'set'
require 'date'
require 'time'

NEWS_PATH = '_data/news.yml'
CONTRIBUTORS_PATH = '_data/CONTRIBUTORS.yaml'
PAGES_DIR = 'pages'
DEFAULT_SUMMARY_PATH = 'var/editors_news_backfill_summary.md'

options = {
  owner: 'elixir-europe',
  repo: 'rdmkit',
  write: false,
  delay: 0.0,
  summary: DEFAULT_SUMMARY_PATH
}

OptionParser.new do |opts|
  opts.banner = 'Usage: ruby var/populate_editors_from_news_prs.rb [options]'
  opts.on('--owner OWNER', 'GitHub owner (default: elixir-europe)') { |v| options[:owner] = v }
  opts.on('--repo REPO', 'GitHub repo (default: rdmkit)') { |v| options[:repo] = v }
  opts.on('--write', 'Write changes to files') { options[:write] = true }
  opts.on('--delay SECONDS', Float, 'Delay between paginated requests') { |v| options[:delay] = v }
  opts.on('--summary PATH', 'Summary markdown output path') { |v| options[:summary] = v }
end.parse!

def github_get(owner, repo, path, params, token)
  uri = URI("https://api.github.com/repos/#{owner}/#{repo}#{path}")
  uri.query = URI.encode_www_form(params)

  req = Net::HTTP::Get.new(uri)
  req['Accept'] = 'application/vnd.github+json'
  req['X-GitHub-Api-Version'] = '2022-11-28'
  req['User-Agent'] = 'rdmkit-editors-backfill-script'
  req['Authorization'] = "Bearer #{token}" if token && !token.empty?

  res = Net::HTTP.start(uri.host, uri.port, use_ssl: true, read_timeout: 30) { |http| http.request(req) }
  unless res.code.to_i.between?(200, 299)
    raise "GitHub API error #{res.code} for #{path}: #{res.body[0, 300]}"
  end

  JSON.parse(res.body)
end

def github_paginated(owner, repo, path, token, delay)
  out = []
  page = 1
  loop do
    payload = github_get(owner, repo, path, { per_page: 100, page: page }, token)
    raise "Unexpected payload for #{path}: expected array" unless payload.is_a?(Array)

    out.concat(payload)
    break if payload.length < 100

    page += 1
    sleep(delay) if delay.positive?
  end
  out
end

def new_page_item?(item)
  item.is_a?(Hash) && item['name'].to_s.strip.downcase.start_with?('new page:')
end

def extract_page_slug(description)
  links = description.to_s.scan(/\[[^\]]+\]\(([^)]+)\)/).flatten
  links.each do |link|
    link = link.to_s.strip
    next if link.start_with?('http://', 'https://', 'mailto:')

    link = link.split('#', 2).first.to_s.strip.sub(%r{^/+}, '').sub(%r{/+$}, '')
    next if link.empty?

    return File.basename(link)
  end
  nil
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
  _start, middle, _tail = split_front_matter(content)
  return {} if middle.nil?

  YAML.safe_load(middle.join, permitted_classes: [Date, Time], aliases: true) || {}
rescue StandardError
  {}
end

def render_editors_line(editors)
  "editors: [#{editors.join(', ')}]\n"
end

def update_editors_line(path, editors, write)
  content = File.read(path, encoding: 'UTF-8')
  start, middle, tail = split_front_matter(content)
  return false if middle.nil?

  new_line = render_editors_line(editors)
  updated = []
  found = false

  middle.each do |line|
    if line.match?(/^editors:\s*/)
      unless found
        updated << new_line
      end
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

  File.write(path, new_content, mode: 'w', encoding: 'UTF-8') if write
  true
end

def unique_preserve_order(values)
  seen = Set.new
  out = []
  values.each do |v|
    next if v.nil? || v.to_s.strip.empty?
    next if seen.include?(v)

    seen.add(v)
    out << v
  end
  out
end

def resolve_page_file(slug)
  exact = Dir.glob(File.join(PAGES_DIR, '**', "#{slug}.md")).sort
  return exact[0] unless exact.empty?

  Dir.glob(File.join(PAGES_DIR, '**', '*.md')).sort.each do |path|
    fm = read_front_matter(path)
    return path if fm['page_id'].to_s.strip == slug
  end
  nil
end

def write_summary(path, rows, options)
  page_to_url = lambda do |page|
    return '' if page.to_s.strip.empty?
    slug = File.basename(page.to_s, '.md')
    "[#{page}](https://rdmkit.elixir-europe.org/#{slug})"
  end

  lines = []
  lines << '# Editors Backfill Summary (News-Based)'
  lines << ''
  lines << "- Generated: #{Time.now.utc.iso8601}"
  lines << "- Repo: `#{options[:owner]}/#{options[:repo]}`"
  lines << "- Mode: #{options[:write] ? 'write' : 'dry-run'}"
  lines << ''
  lines << '| Page | Chosen PR | Editors |'
  lines << '|---|---:|---|'

  rows.each do |r|
    page_col = page_to_url.call(r[:page] || '')
    pr_col = if r[:pr]
               "[##{r[:pr]}](https://github.com/#{options[:owner]}/#{options[:repo]}/pull/#{r[:pr]})"
             else
               ''
             end
    editors_col = r[:editors].empty? ? '' : r[:editors].join(', ')
    lines << "| #{page_col} | #{pr_col} | #{editors_col} |"
  end

  File.write(path, lines.join("\n") + "\n", mode: 'w', encoding: 'UTF-8')
end

news = YAML.safe_load(File.read(NEWS_PATH, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || []
contributors = YAML.safe_load(File.read(CONTRIBUTORS_PATH, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}

targets = []
news.each do |item|
  next unless new_page_item?(item)

  pr = item['linked_pr']
  pr = pr.to_i if pr.is_a?(String) && pr.match?(/^\d+$/)
  next unless pr.is_a?(Integer) && pr.positive?

  slug = extract_page_slug(item['description'])
  next if slug.nil? || slug.empty?

  targets << { pr: pr, slug: slug, name: item['name'].to_s }
end

if targets.empty?
  warn "No 'New page' news items with linked PR and page link found."
  exit 0
end

editors_by_git = {}
contributors.each do |full_name, meta|
  next unless meta.is_a?(Hash)
  next unless meta['role'].to_s.strip.downcase == 'editor'

  git = meta['git'].to_s.strip.downcase
  next if git.empty?

  editors_by_git[git] = full_name.to_s
end

if editors_by_git.empty?
  warn 'No contributors with role=editor and git id found in contributors file.'
  exit 1
end

token = ENV['GITHUB_TOKEN'] || ENV['GH_TOKEN']
changed = 0
skipped = 0
rows = []

puts "Found #{targets.length} new-page news items."

targets.each do |target|
  page_file = resolve_page_file(target[:slug])
  if page_file.nil?
    skipped += 1
    rows << { page: target[:slug], pr: target[:pr], editors: [], status: 'page_not_found' }
    puts "[skip] PR ##{target[:pr]}: could not resolve page slug '#{target[:slug]}'"
    next
  end

  begin
    people = Set.new

    # Approvals and review submissions on the PR.
    reviews = github_paginated(options[:owner], options[:repo], "/pulls/#{target[:pr]}/reviews", token, options[:delay])
    reviews.each do |review|
      user = review.is_a?(Hash) ? review['user'] : nil
      login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
      state = review.is_a?(Hash) ? review['state'].to_s.upcase : ''
      people << login if !login.empty? && %w[APPROVED COMMENTED CHANGES_REQUESTED].include?(state)
    end

    # Conversation comments on the PR issue thread.
    issue_comments = github_paginated(options[:owner], options[:repo], "/issues/#{target[:pr]}/comments", token, options[:delay])
    issue_comments.each do |comment|
      user = comment.is_a?(Hash) ? comment['user'] : nil
      login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
      people << login unless login.empty?
    end

    # Inline review comments on changed lines.
    pr_comments = github_paginated(options[:owner], options[:repo], "/pulls/#{target[:pr]}/comments", token, options[:delay])
    pr_comments.each do |comment|
      user = comment.is_a?(Hash) ? comment['user'] : nil
      login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
      people << login unless login.empty?
    end

    matched = people.to_a.sort.map { |login| editors_by_git[login] }.compact
    matched = unique_preserve_order(matched)

    if matched.empty?
      skipped += 1
      rows << { page: page_file, pr: target[:pr], editors: [], status: 'no_matching_editor' }
      puts "[skip] PR ##{target[:pr]} -> #{page_file}: no matching editors found"
      next
    end

    fm = read_front_matter(page_file)
    existing = fm['editors']
    merged = if existing.is_a?(Array)
               unique_preserve_order(existing + matched)
             elsif existing.is_a?(String) && !existing.strip.empty?
               unique_preserve_order([existing.strip] + matched)
             else
               matched
             end

    did_change = update_editors_line(page_file, merged, options[:write])
    rows << { page: page_file, pr: target[:pr], editors: merged, status: (did_change ? 'updated' : 'unchanged') }
    puts "[#{did_change ? 'updated' : 'unchanged'}] PR ##{target[:pr]} -> #{page_file}: editors=#{merged.inspect}"
    changed += 1 if did_change
  rescue StandardError => e
    skipped += 1
    rows << { page: page_file, pr: target[:pr], editors: [], status: "error: #{e.message.gsub('|', '/')}" }
    puts "[skip] PR ##{target[:pr]} (#{page_file}): #{e}"
  end
end

write_summary(options[:summary], rows, options)
puts "Summary written to #{options[:summary]}"
puts "Done. #{options[:write] ? 'Wrote' : 'Dry-run detected'} changes for #{changed} page(s); skipped #{skipped}."
