import requests

# GitHub API endpoint for creating a comment
COMMENT_URL = "https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"

# GitHub personal access token
TOKEN = ""

# GitHub repository information
owner = "elixir-europe"
repo = "rdmkit"

def add_comment_to_issue(issue_id, comment):
    # URL for creating a comment on a specific issue
    url = COMMENT_URL.format(owner=owner, repo=repo, issue_number=issue_id)

    # Headers with authentication token
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Comment payload
    payload = {
        "body": comment
    }

    # Send POST request to create the comment
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Comment added to issue #{issue_id}")
    else:
        print(f"Failed to add comment to issue #{issue_id}")
        print(response.json())

# Iterate over the list of issue IDs and add a comment to each issue
for issue_id in range(1296, 1327 + 1):
    comment_text = "We will move to the new system in the week of the 24th of Juli, so please make sure changes are comments are made before this date. Thanks a lot in advance!"
    add_comment_to_issue(issue_id, comment_text)