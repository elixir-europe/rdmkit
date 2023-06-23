import csv
import os
import yaml
import frontmatter
import requests

def read_csv_file(filename):
    tools = {}
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            tool_name = row['Orphan tool']
            tags = row['Related_pages'].split(',')
            description = row['Orphan tool description']
            url = row['tool link']
            for tag in tags:
                tag = tag.strip()
                if tag not in tools:
                    tools[tag] = []
                tools[tag].append({'name' : tool_name, 'description' :description, 'url' : url })
    
    return tools

def render_body(tool_list, contributors, text):
    output = f"### Page: [{contributors['title']}]({contributors['file']})\n\n"
    output +=  f"{text}\n\n**Tools that are not mentioned in the text:**\n"
    for tool in tool_list:
        output += f'- [ ] **[{tool["name"]}]({tool["url"]})** - {tool["description"]}\n'
    output += f"\n\nWould you kindly review these tools and determine if they should be mentioned (as a link) in the text? If necessary, please propose changes to the text through a pull request on this temporary [instance of the RDMkit](https://bedroesb.github.io/rdmkit) by clicking on the pencil icon next to the title and following the instructions in this [guide](https://bedroesb.github.io/rdmkit/tool_resource_update). {', '.join(contributors['contributors'])}\n"
    return output


def lookup_git_id(contributor, contributors_file):
    if contributor in contributors_file and 'git' in contributors_file[contributor] and contributors_file[contributor]['git']:
        return contributors_file[contributor]['git']
    else:
        return False


def get_contributors(markdown_dir, contributors_file):
    with open(contributors_file, 'r') as yaml_file:
        contributors_data = yaml.safe_load(yaml_file)

    page_contributors = {}
    
    for root, dirs, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_file = os.path.join(root, file)
                with open(markdown_file, 'r') as file_content:
                    post = frontmatter.load(file_content)
                    front_matter = post.metadata
                    if 'page_id' in front_matter and 'contributors' in front_matter:
                        contributors = front_matter['contributors']
                        page_id = front_matter['page_id']
                        title = front_matter['title']
                        file_name = file.removesuffix(".md")
                        contr_ids = []
                        for contributor in contributors:
                            git_id = lookup_git_id(contributor, contributors_data)
                            if git_id:
                                contr_ids.append(f"@{git_id}")
                        page_contributors[page_id] = {}
                        page_contributors[page_id]['contributors'] = contr_ids
                        page_contributors[page_id]['file'] = f"https://rdmkit.elixir-europe.org/{file_name}"
                        page_contributors[page_id]['title'] = title      
    return page_contributors


def create_github_issue(repo_owner, repo_name, title, body, token, labels):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body,
        "labels": labels
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        issue_data = response.json()
        issue_number = issue_data["number"]
        print(f"Successfully created GitHub issue #{issue_number}")
    else:
        print("Failed to create GitHub issue")
        print(f"Response: {response.status_code} - {response.text}")


# Usage
filename = '/home/bedro/Documents/rdmkit/_data/tool_and_resource_list.csv'
markdown_dir = '/home/bedro/Documents/rdmkit/pages'
contributors_file = '/home/bedro/Documents/rdmkit/_data/CONTRIBUTORS.yaml'

# Github info
repo_owner = "elixir-europe"
repo_name = "rdmkit"
body = "In pull request #1249, we are implementing changes to how we handle tools, resulting in different rules for rendering the tools table at the bottom of pages. Going forward, only tools referenced in the text will be included in the bottom table of the page. Some of the tools have been tagged with the page_id of this page, and we are currently exploring how to incorporate these tools into the text."
tags = ["tool-text-discrepancy"]
token = ""
whitelist = ["data_publication"]


tools = read_csv_file(filename)
page_contributors = get_contributors(markdown_dir, contributors_file)


for tag, tool_list in tools.items():
    if tag in page_contributors and tag not in whitelist:
        output = render_body(tool_list, page_contributors[tag], body)
        title = f"{page_contributors[tag]['title']}: tools not mentioned in in text"
        create_github_issue(repo_owner, repo_name, title, output, token, tags)
    else:
        print(f"{tag} could not be found")
