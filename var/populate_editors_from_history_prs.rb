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
require 'open3'

CONTRIBUTORS_PATH = '_data/CONTRIBUTORS.yaml'
DEFAULT_SUMMARY_PATH = 'var/editors_history_backfill_summary.md'
ELIGIBLE_ROOTS = [
  'pages/your_domain',
  'pages/your_tasks',
  'pages/tool_assembly',
  'pages/national_resources',
  'pages/your_role',
  'pages/data_life_cycle'
].freeze

options = {
  owner: 'elixir-europe',
  repo: 'rdmkit',
  write: false,
  delay: 0.0,
  summary: DEFAULT_SUMMARY_PATH
}

OptionParser.new do |opts|
  opts.banner = 'Usage: ruby var/populate_editors_from_history_prs.rb [options]'
  opts.on('--owner OWNER', 'GitHub owner (default: elixir-europe)') { |v| options[:owner] = v }
  opts.on('--repo REPO', 'GitHub repo (default: rdmkit)') { |v| options[:repo] = v }
  opts.on('--write', 'Write changes to files') { options[:write] = true }
  opts.on('--delay SECONDS', Float, 'Delay between API calls') { |v| options[:delay] = v }
  opts.on('--summary PATH', 'Summary markdown output path') { |v| options[:summary] = v }
end.parse!

def github_get(owner, repo, path, params, token)
  uri = URI("https://api.github.com/repos/#{owner}/#{repo}#{path}")
  uri.query = URI.encode_www_form(params) unless params.empty?

  req = Net::HTTP::Get.new(uri)
  req['Accept'] = 'application/vnd.github+json'
  req['X-GitHub-Api-Version'] = '2022-11-28'
  req['User-Agent'] = 'rdmkit-editors-history-backfill-script'
  req['Authorization'] = "Bearer #{token}" if token && !token.empty?

  res = Net::HTTP.start(uri.host, uri.port, use_ssl: true, read_timeout: 30) { |http| http.request(req) }
  unless res.code.to_i.between?(200, 299)
    raise "GitHub API error #{res.code} for #{path}: #{res.body.to_s[0, 300]}"
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

def eligible_pages_missing_editors
  out = []
  ELIGIBLE_ROOTS.each do |root|
    Dir.glob(File.join(root, '**', '*.md')).sort.each do |path|
      next if File.basename(path).start_with?('TEMPLATE_')

      fm = read_front_matter(path)
      editors = fm['editors']
      has_editors = editors.is_a?(Array) ? !editors.empty? : (editors.is_a?(String) && !editors.strip.empty?)
      out << path unless has_editors
    end
  end
  out
end

def commit_additions_for_file(path)
  cmd = ['git', 'log', '--follow', '--numstat', '--format=commit %H', '--', path]
  stdout, stderr, status = Open3.capture3(*cmd)
  raise "git log failed for #{path}: #{stderr}" unless status.success?

  commits = []
  current = nil
  current_additions = 0

  stdout.each_line do |line|
    line = line.chomp
    if line.start_with?('commit ')
      commits << [current, current_additions] if current
      current = line.split(' ', 2)[1]
      current_additions = 0
      next
    end

    next if line.strip.empty?

    parts = line.split("\t")
    next unless parts.length >= 3

    add_str = parts[0]
    additions = add_str.match?(/^\d+$/) ? add_str.to_i : 0
    current_additions += additions
  end

  commits << [current, current_additions] if current
  commits
end

def pr_numbers_for_commit(owner, repo, sha, token)
  payload = github_get(owner, repo, "/commits/#{sha}/pulls", {}, token)
  return [] unless payload.is_a?(Array)

  payload.map { |pr| pr.is_a?(Hash) ? pr['number'] : nil }.compact
end

def title_for_commit(sha)
  stdout, _stderr, status = Open3.capture3('git', 'show', '-s', '--format=%s', sha)
  return '' unless status.success?

  stdout.to_s.strip
end

def extract_pr_from_title(title)
  m = title.match(/\(#(\d+)\)\s*$/)
  return nil if m.nil?

  m[1].to_i
end

def choose_pr_for_page(owner, repo, page_path, token, commit_pr_cache, delay)
  commits = commit_additions_for_file(page_path)
  commits = commits.sort_by { |_sha, add| -add }

  commits.each do |sha, additions|
    next if sha.nil?

    prs = commit_pr_cache.fetch(sha) do
      found = pr_numbers_for_commit(owner, repo, sha, token)
      commit_pr_cache[sha] = found
      sleep(delay) if delay.positive?
      found
    end

    unless prs.empty?
      return { pr: prs.first, sha: sha, additions: additions, reason: 'commit_association' }
    end

    title = title_for_commit(sha)
    pr_from_title = extract_pr_from_title(title)
    return { pr: pr_from_title, sha: sha, additions: additions, reason: 'commit_title' } if pr_from_title
  end

  nil
end

def participants_for_pr(owner, repo, pr_number, token, delay, pr_participants_cache)
  cached = pr_participants_cache[pr_number]
  return cached unless cached.nil?

  people = Set.new

  reviews = github_paginated(owner, repo, "/pulls/#{pr_number}/reviews", token, delay)
  reviews.each do |review|
    user = review.is_a?(Hash) ? review['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    state = review.is_a?(Hash) ? review['state'].to_s.upcase : ''
    people << login if !login.empty? && %w[APPROVED COMMENTED CHANGES_REQUESTED].include?(state)
  end

  issue_comments = github_paginated(owner, repo, "/issues/#{pr_number}/comments", token, delay)
  issue_comments.each do |comment|
    user = comment.is_a?(Hash) ? comment['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    people << login unless login.empty?
  end

  pr_comments = github_paginated(owner, repo, "/pulls/#{pr_number}/comments", token, delay)
  pr_comments.each do |comment|
    user = comment.is_a?(Hash) ? comment['user'] : nil
    login = user.is_a?(Hash) ? user['login'].to_s.downcase : ''
    people << login unless login.empty?
  end

  pr_participants_cache[pr_number] = people.to_a.sort
  people.to_a.sort
end

def write_summary(path, rows, options)
  page_to_url = lambda do |page|
    return '' if page.to_s.strip.empty?
    slug = File.basename(page.to_s, '.md')
    "[#{page}](https://rdmkit.elixir-europe.org/#{slug})"
  end

  lines = []
  lines << '# Editors Backfill Summary (History-Based)'
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

contributors = YAML.safe_load(File.read(CONTRIBUTORS_PATH, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}
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

pages = eligible_pages_missing_editors
if pages.empty?
  puts 'No eligible pages without editors found.'
  write_summary(options[:summary], [], options)
  exit 0
end

token = ENV['GITHUB_TOKEN'] || ENV['GH_TOKEN']
commit_pr_cache = {}
pr_participants_cache = {}
rows = []
changed = 0
skipped = 0

puts "Found #{pages.length} eligible pages without editors."

pages.each do |page|
  begin
    chosen = choose_pr_for_page(options[:owner], options[:repo], page, token, commit_pr_cache, options[:delay])
    if chosen.nil?
      skipped += 1
      rows << { page: page, pr: nil, sha: nil, additions: nil, editors: [], status: 'no_pr_found' }
      puts "[skip] #{page}: no PR could be associated from git history"
      next
    end

    participants = participants_for_pr(options[:owner], options[:repo], chosen[:pr], token, options[:delay], pr_participants_cache)
    matched = participants.map { |login| editors_by_git[login] }.compact
    matched = unique_preserve_order(matched)

    if matched.empty?
      skipped += 1
      rows << { page: page, pr: chosen[:pr], sha: chosen[:sha], additions: chosen[:additions], editors: [], status: 'no_matching_editor' }
      puts "[skip] #{page}: PR ##{chosen[:pr]} has no participants mapped to role=editor"
      next
    end

    did_change = update_editors_line(page, matched, options[:write])
    rows << { page: page, pr: chosen[:pr], sha: chosen[:sha], additions: chosen[:additions], editors: matched, status: (did_change ? 'updated' : 'unchanged') }
    changed += 1 if did_change
    puts "[#{did_change ? 'updated' : 'unchanged'}] #{page}: PR ##{chosen[:pr]} -> editors=#{matched.inspect}"
  rescue StandardError => e
    skipped += 1
    rows << { page: page, pr: nil, sha: nil, additions: nil, editors: [], status: "error: #{e.message.gsub('|', '/')}" }
    puts "[skip] #{page}: #{e.message}"
  end
end

write_summary(options[:summary], rows, options)
puts "Summary written to #{options[:summary]}"
puts "Done. #{options[:write] ? 'Wrote' : 'Dry-run detected'} changes for #{changed} page(s); skipped #{skipped}."
