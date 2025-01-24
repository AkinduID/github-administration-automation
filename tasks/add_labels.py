import requests
import json

def add_labels(repo_name, labels, token):
    url = f"https://api.github.com/repos/{repo_name}/labels"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    results = []
    for label in labels:
        response = requests.post(url, headers=headers, data=json.dumps(label))
        if response.status_code == 201:
            results.append(f"Label '{label['name']}' created successfully")
        else:
            results.append(f"Failed to create label '{label['name']}': {response.status_code} - {response.text}")
    return results


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
