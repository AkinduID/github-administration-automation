import requests
import json

# Function Description: Defines Labels for the repository
# Parameters:
#     repo (str): The repository in the format 'owner/repo'.
#     token (str): Personal access token for GitHub authentication.
#     labels (list): A list of dictionaries where each dictionary contains 'name' and 'color' keys.

# ToDO

Labels = [
        # Type labels
        {"name": "Type/Bug", "color": "1d76db"},
        {"name": "Type/New Feature", "color": "1d76db"},
        {"name": "Type/Epic", "color": "1d76db"},
        {"name": "Type/Improvement", "color": "1d76db"},
        {"name": "Type/Task", "color": "1d76db"},
        {"name": "Type/UX", "color": "1d76db"},
        {"name": "Type/Question", "color": "1d76db"},
        {"name": "Type/Docs", "color": "1d76db"},

        # Severity labels
        {"name": "Severity/Blocker", "color": "b60205"},
        {"name": "Severity/Critical", "color": "b60205"},
        {"name": "Severity/Major", "color": "b60205"},
        {"name": "Severity/Minor", "color": "b60205"},
        {"name": "Severity/Trivial", "color": "b60205"},

        # Priority labels
        {"name": "Priority/Highest", "color": "ff9900"},
        {"name": "Priority/High", "color": "ff9900"},
        {"name": "Priority/Normal", "color": "ff9900"},
        {"name": "Priority/Low", "color": "ff9900"},

        # Resolution labels
        {"name": "Resolution/Fixed", "color": "93c47d"},
        {"name": "Resolution/Won’t Fix", "color": "93c47d"},
        {"name": "Resolution/Duplicate", "color": "93c47d"},
        {"name": "Resolution/Cannot Reproduce", "color": "93c47d"},
        {"name": "Resolution/Not a bug", "color": "93c47d"},
        {"name": "Resolution/Invalid", "color": "93c47d"},
        {"name": "Resolution/Postponed", "color": "93c47d"},
    ]

def add_labels_to_repo(repo, token, labels=Labels):
    url = f"https://api.github.com/repos/{repo}/labels"
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



# 1. Type Labels
# Type/Bug: Identifies a bug in the project. Color: #1d76db
# Type/New Feature: Represents a request or task for a new feature. Color: #1d76db
# Type/Epic: Denotes an epic, which is a large body of work that encompasses multiple tasks. Color: #1d76db
# Type/Improvement: Marks enhancements or improvements to existing features. Color: #1d76db
# Type/Task: General task that does not fit into other categories. Color: #1d76db
# Type/UX: Refers to user experience-related tasks or issues. Color: #1d76db
# Type/Question: Highlights queries or clarifications needed. Color: #1d76db
# Type/Docs: Indicates documentation-related tasks or updates. Color: #1d76db

# 2. Severity Labels
# Severity/Blocker: Represents a blocking issue that prevents progress. Color: #b60205
# Severity/Critical: Indicates a critical problem requiring immediate attention. Color: #b60205
# Severity/Major: Highlights major issues but not blockers. Color: #b60205
# Severity/Minor: Marks minor issues or inconveniences. Color: #b60205
# Severity/Trivial: Denotes very low-impact issues. Color: #b60205

# 3. Priority Labels
# Priority/Highest: Urgent tasks requiring immediate action. Color: #ff9900
# Priority/High: High-priority tasks to be completed soon. Color: #ff9900
# Priority/Normal: Tasks with a normal priority level. Color: #ff9900
# Priority/Low: Low-priority tasks that can be deferred. Color: #ff9900

# 4. Resolution Labels
# Resolution/Fixed: Indicates issues that have been resolved. Color: #93c47d
# Resolution/Won’t Fix: Marks issues that will not be addressed. Color: #93c47d
# Resolution/Duplicate: Denotes duplicate issues. Color: #93c47d
# Resolution/Cannot Reproduce: Issues that could not be replicated. Color: #93c47d
# Resolution/Not a Bug: Specifies that the reported issue is not a bug. Color: #93c47d
# Resolution/Invalid: Marks invalid issues or requests. Color: #93c47d
# Resolution/Postponed: Indicates deferred tasks or issues. Color: #93c47d
