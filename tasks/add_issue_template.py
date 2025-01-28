import requests
import base64

# Function Description: Add an issue template to a GitHub repository

# ToDo
# Test Function
# Support custom branch input; default to 'main'

# Add an issue template to a GitHub repository
# Arguments:
# repo : Repository in the format 'owner/repo'
# token : Personal access token for GitHub authentication
# branch : The branch to which the template is added (default: 'main')

def add_issue_template(org,repo, token, branch="main"):
    url = f"https://api.github.com/repos/{org}/{repo}/contents/issue_template.md"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    # Issue template content
    content = """
**Description:**
<!-- Give a brief description of the issue -->

**Suggested Labels:**
<!-- Optional comma separated list of suggested labels. Non committers can't assign labels to issues, so this will help issue creators who are not a committer to suggest possible labels-->

**Suggested Assignees:**
<!--Optional comma separated list of suggested team members who should attend the issue. Non committers can't assign issues to assignees, so this will help issue creators who are not a committer to suggest possible assignees-->

**Affected Product Version:**

**OS, DB, other environment details and versions:**    

**Steps to reproduce:**


**Related Issues:**
<!-- Any related issues such as sub tasks, issues reported in other repositories (e.g component repositories), similar problems, etc. -->

"""

    # Encode the content in Base64
    encoded_content = base64.b64encode(content.encode()).decode()

    # JSON payload
    data = {
        "path": "issue_template.md",
        "message": "Add Issue Template",
        "committer": {
            "name": "akindu",
            "email": "akindu@wso2.com"
        },
        "content": encoded_content,
        "branch": branch
    }

    # Send the PUT request
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Issue template added successfully.")
        return response.json()
    else:
        raise Exception(f"Failed to add issue template: {response.status_code}, {response.json()}")

GITHUB_TOKEN = "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"

# # Test the function
# if __name__ == "__main__":
#     org = "Akindu-ID"
#     repo = "test-repo-27"
#     try:
#         response = add_issue_template(org, repo, GITHUB_TOKEN)
#         print(response)
#     except Exception as e:
#         print(e)