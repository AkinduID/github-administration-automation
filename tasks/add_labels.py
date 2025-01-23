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
