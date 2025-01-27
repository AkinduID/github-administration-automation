import requests

# Function Description: Update the topics for a GitHub repository

# ToDo
# Test Function
# check url

def add_topics(org, repo, topics, token):
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

GITHUB_TOKEN = "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"

# Test the function
if __name__ == "__main__":
    owner = "Akindu-ID"
    repo = "test-repo-27"
    topics = ["topic1", "topic2"]
    add_topics(owner, repo, topics, GITHUB_TOKEN)