import requests
import json

import requests
import json

# Function Description: Get the team IDs in an organization and save the data in a JSON file
# Function nis called once and the data is appended to the JSON file. This is to avoid making multiple API calls.
# Input Parameters:
# org: Name of the organization : string
# token: Personal Access Token : string

FILE_NAME = "teams_data.json"

def get_team_ids(org, token):
    url = f"https://api.github.com/orgs/{org}/teams"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        teams_data = response.json()
        
        # Restructure the data as per the required JSON format
        grouped_data = {}
        for team in teams_data:
            lab_name = org
            team_entry = {
                "name": team.get("name"),
                "id": team.get("id")
            }

            if lab_name not in grouped_data:
                grouped_data[lab_name] = []

            grouped_data[lab_name].append(team_entry)

        final_output = [
            {"name": lab, "teams": teams}
            for lab, teams in grouped_data.items()
        ]
        
        try:
            with open(FILE_NAME, "r") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        existing_data.extend(final_output)

        with open(FILE_NAME, "w") as file:
            json.dump(existing_data, file, indent=4)

        print(f"Formatted teams data appended to {FILE_NAME}")
    else:
        print(f"Failed to fetch teams. Status code: {response.status_code}")
        exit(1)


# Configuration
PERSONAL_ACCESS_TOKEN = "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"  # Replace with your personal access token
ORGANIZATION = "GitOpsLab-1"  # Replace with your organization name
FILE_NAME = "tasks/teamid_list.json"  # Replace with your desired JSON file name


# Test
if __name__ == "__main__":
    get_team_ids(ORGANIZATION, PERSONAL_ACCESS_TOKEN)