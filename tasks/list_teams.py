import requests

# Function Description: List the Team IDs for given team names

def list_teams(organization, token):
    url = f"https://api.github.com/orgs/{organization}/teams?per_page=100"
    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch teams: {response.status_code} - {response.text}")
