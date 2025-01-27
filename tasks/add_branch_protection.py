import requests

# Function Description: Protect the main branch of a GitHub repository
# Parameters:
#     org (str): The organization name.
#     repo (str): The repository name.
#     access_token (str): Personal access token for GitHub authentication.

# ToDO
# Test Function
# Private branches cant be protected wihtout a pro account. Check for this condition and return an error message

#branch protection option 1
def add_branch_protection(org, repo, access_token):
    url = f"https://api.github.com/repos/{org}/{repo}/branches/main/protection" #check for url validity
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.loki-preview"
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

# GITHUB_TOKEN = "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"



# # Test the function
# if __name__ == "__main__":
#     org = "Akindu-ID"
#     repo = "test-repo-25"
#     add_branch_protection(org, repo, GITHUB_TOKEN)