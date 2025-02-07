import requests

# Function Description: Set the permissions for the infra team
# Input Parameters:
# org: Name of the organization : string
# repo: Name of the repository : string
# teams: List of teams to be granted access : list
# token: Personal Access Token : string

# ToDo
# select relevent readonly team based on user inputed internal commmiters team

# gitopslab-enterprise
#   gitopslab-all - triage if user inputs else pull
        # internal-committers - write access based on user input
        # readonly - read access based on relevent internal committers team access
#   gitopslab-all-interns - triage if user inputs else pull
#   engineering-readonly-bots - pull
#   infra - push

# gitopslab and all other organizations
#   gitopslab-all - pull 
        # internal-committers - write access based on user input
        # external-committers - write access based on relevent internal committers team access
#   ?gitopslab-all-interns -
#   ?readonly-bots - 
#   infra - push



import json
import requests

def set_team_permissions_ent(org, repo, teams, enable_triage_wso2all,enable_triage_wso2allinterns,token):

    teams.append("Infra")
    teams.append("gitopslab-all")
    teams.append("gitopslab-all-interns")
    teams.append("engineering-readonly-bots")
    readonly_teams = [team.replace("-internal-commiters", "-readonly") for team in teams if "-internal-commiters" in team]
    teams.extend(readonly_teams)

    print(f"Setting permissions for teams {teams} in organization {org} for repo {repo}")
    # Read the JSON file
    with open('app/data/teamids_list.json', 'r') as file:
        team_data = json.load(file)
    # Extract team IDs for the specified teams in the given organization
    team_ids = []
    for lab in team_data:
        if lab['name'] == org:
            for team in lab['teams']:
                print(f"Team: {team['name']}") # Debugging
                if team['name'] in teams:
                    team_ids.append((team['id'],team['name']))
    print(f"Team IDs: {team_ids}")
    if not team_ids:
        print(f"No matching teams found in organization {org}")
        return
    # GitHub API base URL
    api_base_url = "https://api.github.com"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    # Grant permissions to each specified team
    for team_id in team_ids:
        # print(f"Granting access to team ID {team_id} for repo {repo}")
        url = f"{api_base_url}/teams/{team_id[0]}/repos/{org}/{repo}"
        if team_id[1] == "Infra" or team_id[1].endswith("-commiters"):
            payload = {
                "permission": "push"  
            }
        elif (team_id[1] == "gitopslab-all" and enable_triage_wso2all) or (team_id[1] == "gitopslab-all-interns" and enable_triage_wso2allinterns):
            payload = {
                "permission": "triage"  
            }
        else: 
            payload = {
                "permission": "pull" 
            }
        response = requests.put(url, headers=headers, json=payload)
        if response.status_code == 204:
            print(f"Granted {payload} access to team ID {team_id} for repo {repo}")
        else:
            print(f"Failed to grant access to team ID {team_id}. Error: {response.status_code}, {response.text}")