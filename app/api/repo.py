# app/api/repo.py
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models.repo import RepoRequest
from app.utils.file_operation import read_requests, write_requests
from app.tasks.github_operations import create_repo, add_topics, add_labels, add_issue_template, add_pr_template, add_branch_protection, add_branch_protection_bal, set_team_permissions, get_pat
import json

router = APIRouter()

@router.get("/get_teams/{organization}")
def get_teams(organization: str):
    team_list = []
    with open('app/data/teamids_list.json', 'r') as file:
        team_data = json.load(file)
    for org_data in team_data:
        if org_data["name"] == organization:
            for team in org_data["teams"]:
                team_list.append(team["name"])
            return team_list
    raise HTTPException(status_code=404, detail="Organization not found")

@router.post("/create_request")
def create_request(repo: RepoRequest):
    new_request = repo.dict()
    new_request["timestamp"] = datetime.now().isoformat()
    new_request["approval_state"] = "Pending"
    requests_list = read_requests()
    requests_list.append(new_request)
    write_requests(requests_list)
    return {"message": "Repository request created successfully!", "request": new_request}

@router.get("/requests")
def get_requests():
    return read_requests()

@router.post("/approve_request/{repo_name}")
def approve_request(repo_name: str):
    requests_list = read_requests()
    request_exists = False
    for request in requests_list:
        if request["repo_name"] == repo_name:
            request_exists = True
            if request["approval_state"] != "Pending":
                raise HTTPException(status_code=400, detail="Request is already processed")
            try:
                repo_name = request["repo_name"]
                repo_name = repo_name.replace(" ", "-")
                organization = request["organization"]
                organization = organization.replace(" ", "-")
                GITHUB_TOKEN = get_pat(organization)
                print(organization, GITHUB_TOKEN)
                repo_type = request["repo_type"]
                description = request["description"]
                pr_protection = request["pr_protection"]
                enable_issues = request["enable_issues"]
                website_url = request["website_url"]
                topics = request["topics"]
                teams = request["teams"]
                print(repo_name, organization, GITHUB_TOKEN, repo_type, description, pr_protection, enable_issues, website_url, topics, teams)
                # Call GitHub operations
                create_repo(organization, repo_name, description, repo_type, enable_issues, website_url, GITHUB_TOKEN)
                if topics:
                    add_topics(organization, repo_name, topics, GITHUB_TOKEN)
                add_labels(organization, repo_name, GITHUB_TOKEN)
                add_issue_template(organization, repo_name, GITHUB_TOKEN)
                add_pr_template(organization, repo_name, GITHUB_TOKEN)
                if pr_protection:
                    add_branch_protection(organization, repo_name, GITHUB_TOKEN)
                else:
                    add_branch_protection_bal(organization, repo_name, GITHUB_TOKEN)
                set_team_permissions(organization, repo_name, teams, GITHUB_TOKEN) 
                # give admin access to infra team as a default.
                # read only access to wso2 all
                # list internal committers teams
                request["approval_state"] = "Approved"
                write_requests(requests_list)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Repository creation failed: {str(e)}")
            break

    if not request_exists:
        raise HTTPException(status_code=404, detail="Request not found")
