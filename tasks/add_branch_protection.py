import requests

# Function Description: Protect the main branch of a GitHub repository
# Parameters:
#     org (str): The organization name.
#     repo (str): The repository name.
#     access_token (str): Personal access token for GitHub authentication.

# ToDO
# Test Function
# Cannot apply protection to private repos without a pro account. Check for this condition

#branch protection option 1
def add_branch_protection(org, repo, access_token):
    url = f"https://api.github.com/repos/{org}/{repo}/branches/main/protection" #check for url validity
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/vnd.github+json"

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
# def add_branch_protection_bal(org, repo, access_token):
#     url = f"https://api.github.com/repos/{org}/{repo}"
#     headers = {
#         "Authorization": f"token {access_token}",
#         "Accept": "application/vnd.github.v3+json"
#     }
#     data = {
#         "has_issues": False,
#         "has_projects": False
#     }

#     response = requests.patch(url, json=data, headers=headers)

#     if response.status_code == 200:
#         print("Main branch protected for ballerina repo")
#     else:
#         print(f"Failed to update repo settings: {response.status_code}, {response.text}")

# GITHUB_TOKEN = "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xx"



# # Test the function
# if __name__ == "__main__":
#     org = "GitOpsLab-1"
#     repo = "test-repo-13"
#     add_branch_protection(org, repo, GITHUB_TOKEN)