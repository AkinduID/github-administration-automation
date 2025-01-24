import requests

GITHUB_TOKEN = "YOUR-TOKEN"
OWNER = "OWNER"
REPO = "REPO"
TOPICS = ["octocat", "atom", "electron", "api"]
url = f"https://api.github.com/repos/{OWNER}/{REPO}/topics"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.mercy-preview+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
payload = {
    "names": TOPICS
}
response = requests.put(url, json=payload, headers=headers)
if response.status_code == 200:
    print("Topics updated successfully!")
else:
    print(f"Failed to update topics. Status code: {response.status_code}")
    print("Response:", response.json())

def add_topics(repo_name, topics, token):
    pass