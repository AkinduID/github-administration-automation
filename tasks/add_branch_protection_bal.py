import requests

# Function Description: Protect the main branch of a GitHub repository
# Parameters:
#     org (str): The organization name.
#     repo (str): The repository name.
#     access_token (str): Personal access token for GitHub authentication.

# ToDO
# Test Function
# Private branches cant be protected wihtout a pro account. Check for this condition and return an error message



# branch protection option 2
def add_branch_protection_bal(org, repo, access_token):
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

# GITHUB_TOKEN = "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xx"



# # Test the function
# if __name__ == "__main__":
#     org = "GitOpsLab-1"
#     repo = "test-repo-13"
#     add_branch_protection_bal(org, repo, GITHUB_TOKEN)