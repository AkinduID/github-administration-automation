import requests

# Function Description: Update the topics for a GitHub repository
# Input Parameters:
# org: Name of the organization : string
# repo: Name of the repository : string
# topics: List of topics to be added to the repository : list
# token: Personal Access Token : string

# ToDo
# Test Function
# check url

def add_topics(org, repo, topics, token):
    print(f"Adding topics to the repository: {org} {repo}, {topics}")
    url = f"https://api.github.com/repos/{org}/{repo}/topics"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    data = {"names": topics}
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Repository topics updated successfully.")
    else:
        print(f"Failed to update topics. Status code: {response.status_code}")
        print(response.json())

#################################################################################################################

# GITHUB_TOKEN = "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xy"

# # Test the function
# if __name__ == "__main__":
#     owner = "GitOpsLab-2"
#     repo = "test-repo-01"
#     topics = ["topic1", "topic2"]
#     add_topics(owner, repo, topics, GITHUB_TOKEN)