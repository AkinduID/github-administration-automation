import requests
import json

# Function Description: Create a new repository in the organization

# ToDO
# remove team id from the payload done. create separate function in set_infra_teams.py file
# add url to payload done. set if given else ignore

# Create a new repository in the organization
# Data to be sent as JSON payload
# name : repo_name
# description : repo_desc
# private : true of false
# homepage: website_url (optional)
# has_issues: enable_issues
# has_wiki : false (default)
# auto_init : true (default)
# gitignore_template : Java (default)
# license_template : apache-2.0 (default)

def create_repo(organization, repo_name, repo_desc, private, enable_issues,website_url, token):
    url = f"https://api.github.com/orgs/{organization}/repos"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": repo_name,
        "description": repo_desc,
        "private": private,
        "homepage": website_url, #optional
        "has_issues": enable_issues,
        # default values
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


# GITHUB_TOKEN = "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"

# # Test the function
# if __name__ == "__main__":
#     org = "Akindu-ID"
#     repo_name = "test-repo-15"
#     repo_desc = "This is a test repository"
#     private = False
#     enable_issues = True
#     website_url = "https://github.com"
#     try:
#         response = create_repo(org, repo_name, repo_desc, private, enable_issues, website_url, GITHUB_TOKEN)
#         print(response)
#     except Exception as e:
#         print(e)