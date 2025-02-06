import requests

# Function Description: Protect the main branch of a GitHub repository
# Input Parameters:
# org: Name of the organization : string
# repo: Name of the repository : string
# access_token: Personal Access Token : string


# ToDO
# Test Function
# Cannot apply protection to private repos without a pro account. Check for this condition

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

####################################################################################################################

# GITHUB_TOKEN = "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xxxl"
# # Test the function
# if __name__ == "__main__":
#     org = "GitOpsLab-1"
#     repo = "test-repo-13"
#     add_branch_protection(org, repo, GITHUB_TOKEN)