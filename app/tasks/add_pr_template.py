import requests
import base64

# Function Description: Add a pull request template to a GitHub repository
# Input Parameters:
# org: Name of the organization : string
# repo: Name of the repository : string
# token: Personal Access Token : string
# branch: The branch to which the template is added (default: 'main') : string

# ToDo
# - Test Function
# - Support custom branch input; default to 'main'

def add_pr_template(org,repo, token):
    url = f"https://api.github.com/repos/{org}/{repo}/contents/pull_request_template.md"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    content = """
## Purpose
> Describe the problems, issues, or needs driving this feature/fix and include links to related issues in the following format: Resolves issue1, issue2, etc.

## Goals
> Describe the solutions that this feature/fix will introduce to resolve the problems described above

## Approach
> Describe how you are implementing the solutions. Include an animated GIF or screenshot if the change affects the UI (email documentation@wso2.com to review all UI text). Include a link to a Markdown file or Google doc if the feature write-up is too long to paste here.

## User stories
> Summary of user stories addressed by this change>

## Release note
> Brief description of the new feature or bug fix as it will appear in the release notes

## Documentation
> Link(s) to product documentation that addresses the changes of this PR. If no doc impact, enter “N/A” plus brief explanation of why there’s no doc impact

## Training
> Link to the PR for changes to the training content in https://github.com/wso2/WSO2-Training, if applicable

## Certification
> Type “Sent” when you have provided new/updated certification questions, plus four answers for each question (correct answer highlighted in bold), based on this change. Certification questions/answers should be sent to certification@wso2.com and NOT pasted in this PR. If there is no impact on certification exams, type “N/A” and explain why.

## Marketing
> Link to drafts of marketing content that will describe and promote this feature, including product page changes, technical articles, blog posts, videos, etc., if applicable

## Automation tests
- Unit tests 
> Code coverage information
- Integration tests
> Details about the test cases and coverage

## Security checks
- Followed secure coding standards in http://wso2.com/technical-reports/wso2-secure-engineering-guidelines? yes/no
- Ran FindSecurityBugs plugin and verified report? yes/no
- Confirmed that this PR doesn't commit any keys, passwords, tokens, usernames, or other secrets? yes/no

## Samples
> Provide high-level details about the samples related to this feature

## Related PRs
> List any other related PRs

## Migrations (if applicable)
> Describe migration steps and platforms on which migration has been tested

## Test environment
> List all JDK versions, operating systems, databases, and browser/versions on which this feature/fix was tested

## Learning
> Describe the research phase and any blog posts, patterns, libraries, or add-ons you used to solve the problem.
"""
    encoded_content = base64.b64encode(content.encode()).decode()
    data = {
        "path": "pull_request_template.md",
        "message": "Add Pull Request Template",
        "committer": {
            "name": "akindu",
            "email": "akindu@wso2.com"
        },
        "content": encoded_content,
        "branch": "main"
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        print("Pull request template added successfully.")
        return response.json()
    else:
        raise Exception(f"Failed to add pull request template: {response.status_code}, {response.json()}")

#################################################################################################################

# GITHUB_TOKEN = "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"

# # Test the function
# if __name__ == "__main__":
#     org = "Akindu-ID"
#     repo = "test-repo-27"
#     try:
#         response = add_pr_template(org, repo, GITHUB_TOKEN)
#         print(response)
#     except Exception as e:
#         print(e)