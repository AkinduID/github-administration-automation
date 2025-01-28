import requests
import json

def get_team_ids(org,token):
    url = f"https://api.github.com/orgs/{org}/teams"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams_data = response.json()
        with open(FILE_NAME, "w") as file:
            json.dump(teams_data, file, indent=4)
            print(f"Teams data saved to {FILE_NAME}")
    else:
        print(f"Failed to fetch teams. Status code: {response.status_code}")
        exit(1)
    with open(FILE_NAME, "r") as file:
        teams_data = json.load(file)

    filtered_data = [{"name": team.get("name"), "id": team.get("id")} for team in teams_data]
    with open(FILE_NAME, "w") as file:
        json.dump(filtered_data, file, indent=4)

    print("Completed listing team IDs!")


# Configuration
PERSONAL_ACCESS_TOKEN = "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"  # Replace with your personal access token
ORGANIZATION = "GitOpsLab-1"  # Replace with your organization name
FILE_NAME = "tasks/teamid_list.json"  # Replace with your desired JSON file name


# Test
if __name__ == "__main__":
    get_team_ids(ORGANIZATION, PERSONAL_ACCESS_TOKEN)