import requests

# Replace these with your details
GITHUB_TOKEN = "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"
ORG_NAME = "Akindu-ID"

# GitHub API base URL
BASE_URL = "https://api.github.com"

def get_org_repos(org_name):
    """Fetch all repositories in the organization."""
    url = f"{BASE_URL}/orgs/{org_name}/repos"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    repos = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            raise Exception(f"Failed to fetch repositories: {response.json().get('message', 'Unknown error')}")
        
        data = response.json()
        if not data:  # Break if no more repositories
            break

        repos.extend(data)
        page += 1

    return repos

def delete_repo(org_name, repo_name):
    """Delete a specific repository in the organization."""
    url = f"{BASE_URL}/repos/{org_name}/{repo_name}"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Deleted repository: {repo_name}")
    else:
        print(f"Failed to delete {repo_name}: {response.json().get('message', 'Unknown error')}")

def delete_all_repos(org_name):
    """Delete all repositories in the organization."""
    try:
        repos = get_org_repos(org_name)
        if not repos:
            print("No repositories found in the organization.")
            return

        print(f"Found {len(repos)} repositories. Deleting...")
        for repo in repos:
            delete_repo(org_name, repo['name'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    confirmation = input(f"Are you sure you want to delete all repositories in the '{ORG_NAME}' organization? (yes/no): ")
    if confirmation.lower() == "yes":
        delete_all_repos(ORG_NAME)
    else:
        print("Operation canceled.")
