import requests

# Function Description: Set the permissions for the infra team

# when an repo is created list the teams of org and give them relevent permissions

# ToDo
# give different permissions to different teams

import json
import requests

def set_team_permissions(org, repo, teams, token):
    print(f"Setting permissions for teams {teams} in organization {org} for repo {repo}")
    # Read the JSON file
    with open('tasks/teamid_list.json', 'r') as file:
        team_data = json.load(file)
    
    # Extract team IDs for the specified teams in the given organization
    team_ids = []
    for lab in team_data:
        if lab['name'] == org:
            for team in lab['teams']:
                print(f"Team: {team['name']}") # Debugging
                if team['name'] in teams:
                    team_ids.append(team['id'])
    print(f"Team IDs: {team_ids}")
    if not team_ids:
        print(f"No matching teams found in organization {org}")
        return

    # GitHub API base URL
    api_base_url = "https://api.github.com"
    
    # Headers for authentication
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    # Grant permissions to each specified team
    for team_id in team_ids:
        print(f"Granting access to team ID {team_id} for repo {repo}")
        url = f"{api_base_url}/teams/{team_id}/repos/{org}/{repo}"
        payload = {
            "permission": "push"  # Possible values: pull, push, admin
        }
        
        response = requests.put(url, headers=headers, json=payload)
        
        if response.status_code == 204:
            print(f"Granted access to team ID {team_id} for repo {repo}")
        else:
            print(f"Failed to grant access to team ID {team_id}. Error: {response.status_code}, {response.text}")

# Example usage
# teams_list = ["GitOPsLabs 1 Team 1", "GitOPsLabs 1 Team 3"]
# set_team_permissions("GitOpsLab-1", "example-repo", "your_github_token", teams_list)


#Adding INFRA GROUP AND READONLY GROUP. Change the team id when different team.
#LINE='wso2-enterprise/asgardeo-subscriptions'
# wso2
# curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/3497524/repos/$LINE?permission=push
# curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/29739/repos/$LINE?permission=push

#select corresponding external-committer team
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/analytics-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/apim-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/ei-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/iam-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/ballerina-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/build-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/choreo-external-committrs/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/ie-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/iot-external-committers/repos/$LINE -d '{"permission":"push"}'
#curl -i -X PUT -H 'Authorization: token <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2/teams/ob-external-committers/repos/$LINE -d '{"permission":"push"}'


#wso2-extensions
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/1924203/repos/$LINE?permission=push
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/2568872/repos/$LINE?permission=push

#wso2-incubator
#curl -i -X PUT -H "" https://api.github.com/teams/698173/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#wso2-enterprise
# curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/3540875/repos/$LINE?permission=push
# curl -X PUT -H "Authorization: token  <PERSONAL_ACCESS_TOKEN>" -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2-enterprise/teams/engineering-readonly-bots/repos/$LINE -d '{"permission":"pull"}'

## uncomment below to grant access wso2-all group
#curl -X PUT -H "Authorization: token  <PERSONAL_ACCESS_TOKEN>" -H "Accept: application/vnd.github.v3+json" https://api.github.com/orgs/wso2-enterprise/teams/wso2-all/repos/$LINE -d '{"permission":"triage"}'

#ballerina-lang
#curl -i -X PUT -H "" https://api.github.com/teams/2246412/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push
#curl -i -X PUT -H "" https://api.github.com/teams/2258127/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#ballerina-lang
#curl -i -X PUT -H "" https://api.github.com/teams/2635734/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#wso2-ballerina
#curl -i -X PUT -H "" https://api.github.com/teams/2632186/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#ballerina-platform
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/2654430/repos/$LINE?permission=push
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/2706154/repos/$LINE?permission=push


#ballerina-guides
#curl -i -X PUT -H "" https://api.github.com/teams/2635734/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

# wso2-support

#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/755929/repos/$LINE?permission=push
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' "" https://api.github.com/teams/1608904/repos/$LINE?permission=push

#wso2-ballerina
#curl -i -X PUT -H "" https://api.github.com/teams/2632186/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#ballerinax
#curl -i -X PUT -H "" https://api.github.com/teams/2672743/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#wso2-cellery
#curl -i -X PUT -H "" https://api.github.com/teams/3036531/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push
#curl -i -X PUT -H "" https://api.github.com/teams/3152752/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#siddhiio
#curl -i -X PUT -H "" https://api.github.com/teams/3115353/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push
#curl -i -X PUT -H "" https://api.github.com/teams/3115344/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#jballerina
#curl -i -X PUT -H "" https://api.github.com/teams/3282241/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push
#curl -i -X PUT -H "" https://api.github.com/teams/3282245/repos/$LINE?access_token= <PERSONAL_ACCESS_TOKEN>&permission=push

#asgardeo
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/teams/4011180/repos/$LINE?permission=push
#curl -i -X PUT -H 'Authorization: token  <PERSONAL_ACCESS_TOKEN>' -H "Accept: application/vnd.github.v3+json" https://api.github.com/teams/4011181/repos/$LINE?permission=push

# echo "granted infra team access"
