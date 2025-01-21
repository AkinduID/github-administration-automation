import requests

# Replace with your GitHub token
GITHUB_TOKEN = "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"
# GITHUB_API_URL = "https://api.github.com/user/repos"
GITHUB_API_URL = "https://api.github.com/orgs/Akindu-ID/repos"

# Repository details
repo_name = "test-repo"
repo_description = "A test repository created via API"
is_private = True

# Headers and payload
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
payload = {
    "name": repo_name,
    "description": repo_description,
    "private": is_private
}

# Make the API request
response = requests.post(GITHUB_API_URL, json=payload, headers=headers)

if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully!")
else:
    print(f"Failed to create repository: {response.json()}")
