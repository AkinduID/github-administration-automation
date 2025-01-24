import requests

#branch protection option 1
def protect_main_branch(repo, access_token):
    url = f"https://api.github.com/repos/{repo}/branches/main/protection" #check for url validity
    headers = {
        "Accept": "application/vnd.github.loki-preview",
    }
    data = {
        "required_status_checks": None,
        "enforce_admins": None,
        "required_pull_request_reviews": {
            "include_admins": False
        },
        "restrictions": None
    }
    params = {
        "access_token": access_token
    }

    response = requests.put(url, json=data, headers=headers, params=params)
    
    if response.status_code == 200:
        print("Main branch protected")
    else:
        print(f"Failed to protect main branch: {response.status_code}, {response.text}")

#branch protection option 2
def update_repo_settings(org, repo, access_token):
    url = f"https://api.github.com/repos/{org}/{repo}"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "has_issues": False,
        "has_projects": False
    }

    response = requests.patch(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Main branch protected for ballerina repo")
    else:
        print(f"Failed to update repo settings: {response.status_code}, {response.text}")