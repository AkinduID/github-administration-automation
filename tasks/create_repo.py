import requests
import json

def create_repo(organization, repo_name, repo_desc, private, group_id, token):
    url = f"https://api.github.com/orgs/{organization}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": repo_name,
        "description": repo_desc,
        "private": private,
        "team_id": group_id,
        "has_wiki": False,
        "auto_init": True,
        "gitignore_template": "Java",
        "license_template": "apache-2.0"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Failed to create repository: {response.status_code} - {response.text}")
