import requests

# GitHub API endpoint for creating a Milestone
MILESTONE_URL = "https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

# GitHub personal access token
TOKEN = ""

# GitHub repository information
owner = "elixir-europe"
repo = "rdmkit"

def add_milestone_to_issue(issue_id, milestone):
    # URL for creating a Milestone on a specific issue
    url = MILESTONE_URL.format(owner=owner, repo=repo, issue_number=issue_id)

    # Headers with authentication token
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Milestone payload
    payload = {
        "milestone": milestone
    }

    # Send POST request to create the Milestone
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Milestone added to issue #{issue_id}")
    else:
        print(f"Failed to add Milestone to issue #{issue_id}")
        print(response.json())

# Iterate over the list of issue IDs and add a milestone to each issue
for issue_id in range(1321, 1327 + 1):
    add_milestone_to_issue(issue_id, 1)