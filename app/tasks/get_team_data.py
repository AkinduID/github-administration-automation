# import requests

# Function Description: List the Team IDs for given team names

# def list_teams(organization, token):
#     url = f"https://api.github.com/orgs/{organization}/teams?per_page=100"
#     headers = {
#         "Authorization": f"token {token}"
#     }

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Failed to fetch teams: {response.status_code} - {response.text}")

import json
import requests

def list_teams():
    # Read pat_list.json
    with open('app/data/pat_list.json', 'r') as file:
        pat_data = json.load(file)
    
    team_ids_list = []

    # For each organization, fetch the teams and their IDs using the PAT
    for org_data in pat_data[0]:  # Looping through the dictionary in the list
        organization = org_data  # Organization name
        pat = pat_data[0][org_data]  # Get the corresponding PAT for the organization
        
        # GitHub API URL for listing teams in an organization
        url = f'https://api.github.com/orgs/{organization}/teams'
        headers = {'Authorization': f'token {pat}'}
        
        # Fetch teams for the organization
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            teams = response.json()
            team_data = []

            for team in teams:
                team_data.append({
                    "name": team['name'],
                    "id": team['id']
                })

            # Append the organization and its teams to the list
            team_ids_list.append({
                "name": organization,
                "teams": team_data
            })
        else:
            print(f"Error fetching teams for {organization}: {response.status_code}")

    # Write team_ids_list to teamids_list.json
    with open('app/data/teamids_list.json', 'w') as outfile:
        json.dump(team_ids_list, outfile, indent=4)
    
    print("teamids_list.json has been created successfully!")

# Run the function
# fetch_teams_and_save()

