import requests

# Function Description: Update the topics for a GitHub repository

# ToDo
# Test Function
# check url

def update_github_repo_topics(token, owner, repo, topics):
    url = f"https://api.github.com/repos/{owner}/{repo}/topics"
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
