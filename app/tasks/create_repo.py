import requests
import json

# Function Description: Create a new repository in the organization
# Input Parameters:
# organization: Name of the organization : string
# repo_name: Name of the repository : string
# repo_desc: Description of the repository : string
# private: True if the repository is private, False if the repository is public : boolean
# enable_issues: True if issues are enabled, False if issues are disabled : boolean
# website_url: URL of the website : string
# token: Personal Access Token : string
# Return: JSON response of the created repository


# ToDO
# remove team id from the payload done. create separate function in set_infra_teams.py file
# add url to payload done. set if given else ignore

# Create a new repository in the organization
# Data to be sent as JSON payload
# name : repo_name
# description : repo_desc
# private : true of false
# homepage: website_url (optional)
# has_issues: enable_issues (true or false)
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
        print("Repository created successfully.")
        return response.json()
    else:
        raise Exception(f"Failed to create repository: {response.status_code} - {response.text}")

#################################################################################################################

# GITHUB_TOKEN = "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xl"

# # Test the function
# if __name__ == "__main__":
#     org = "GitOpsLab-1"
#     repo_name = "test-repo-30"
#     repo_desc = "This is a test repository"
#     private = False
#     enable_issues = True
#     website_url = "https://github.com"
#     try:
#         response = create_repo(org, repo_name, repo_desc, private, enable_issues, website_url, GITHUB_TOKEN)
#         print(response)
#     except Exception as e:
#         print(e)