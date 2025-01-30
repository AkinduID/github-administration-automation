import requests
import json

# Function Description: Defines Labels for the repository
# Input Parameters:
# org: Name of the organization : string
# repo: Name of the repository : string
# token: Personal Access Token : string
# labels: List of labels to be added to the repository : list

# ToDO

Labels = [
        # Type labels
        {"name": "Type/Bug", "color": "1d76db"}, # Identifies a bug in the project
        {"name": "Type/New Feature", "color": "1d76db"}, # Represents a request or task for a new feature
        {"name": "Type/Epic", "color": "1d76db"},  # Denotes an epic, which is a large body of work that encompasses multiple tasks
        {"name": "Type/Improvement", "color": "1d76db"}, # Marks enhancements or improvements to existing features
        {"name": "Type/Task", "color": "1d76db"}, # General task that does not fit into other categories
        {"name": "Type/UX", "color": "1d76db"}, # Refers to user experience-related tasks or issues
        {"name": "Type/Question", "color": "1d76db"}, # Highlights queries or clarifications needed
        {"name": "Type/Docs", "color": "1d76db"}, # Indicates documentation-related tasks or updates
        # Severity labels
        {"name": "Severity/Blocker", "color": "b60205"}, # Represents a blocking issue that prevents progress
        {"name": "Severity/Critical", "color": "b60205"}, # Indicates a critical problem requiring immediate attention
        {"name": "Severity/Major", "color": "b60205"}, # Highlights major issues but not blockers
        {"name": "Severity/Minor", "color": "b60205"}, # Marks minor issues or inconveniences
        {"name": "Severity/Trivial", "color": "b60205"}, # Denotes very low-impact issues
        # Priority labels
        {"name": "Priority/Highest", "color": "ff9900"},   # Urgent tasks requiring immediate action
        {"name": "Priority/High", "color": "ff9900"}, # High-priority tasks to be completed soon
        {"name": "Priority/Normal", "color": "ff9900"}, # Tasks with a normal priority level
        {"name": "Priority/Low", "color": "ff9900"}, # Low-priority tasks that can be deferred
        # Resolution labels
        {"name": "Resolution/Fixed", "color": "93c47d"}, # Indicates issues that have been resolved
        {"name": "Resolution/Won’t Fix", "color": "93c47d"}, # Marks issues that will not be addressed
        {"name": "Resolution/Duplicate", "color": "93c47d"}, # Denotes duplicate issues
        {"name": "Resolution/Cannot Reproduce", "color": "93c47d"}, # Issues that could not be replicated
        {"name": "Resolution/Not a bug", "color": "93c47d"}, # Specifies that the reported issue is not a bug
        {"name": "Resolution/Invalid", "color": "93c47d"}, # Marks invalid issues or requests
        {"name": "Resolution/Postponed", "color": "93c47d"}, # Indicates deferred tasks or issues
    ]

def add_labels(org, repo, token, labels=Labels):
    url = f"https://api.github.com/repos/{org}/{repo}/labels"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    for label in labels:
        response = requests.post(url, headers=headers, json=label)
        if response.status_code == 201:
            print(f"Label '{label['name']}' created successfully.")
        elif response.status_code == 422:
            print(f"Label '{label['name']}' already exists.")
        else:
            print(f"Failed to create label '{label['name']}': {response.status_code}, {response.text}")

###############################################################################################################################

# GITHUB_TOKEN = "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"

# # Test the function
# if __name__ == "__main__":
#     org = "Akindu-ID"
#     repo = "test-repo-27"
#     add_labels(org, repo, GITHUB_TOKEN)

