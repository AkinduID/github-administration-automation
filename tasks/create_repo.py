import requests
import json

# Create a new repository in the organization
# Data to be sent as JSON payload
# name : repo_name, 
# description : repo_desc, 
# private : true of false, 
# team_id : 1234 (list teams and get the id for relevent teams)
# has_wiki : false (default)
# auto_init : true (default)
# gitignore_template : Java (default)
# license_template : apache-2.0 (default)

# More data to be sent as JSON payload
# has_issues
# homepage

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
