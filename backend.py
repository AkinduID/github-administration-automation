from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from datetime import datetime
import json
from functions import create_repo, add_topics, add_labels, add_issue_template, add_pr_template, add_branch_protection, add_branch_protection_bal,set_team_permissions,get_pat

# ToDo
# infra teams permission function
# [x]create multiple org in github and create pats for each org
# [x]create teams in each repo 
# [x]add ability to handle multiple organizatiomns and multipel pat
# [x]create get pat fuction

REQUESTS_FILE = "repo_requests.json"

app = FastAPI()

# GITHUB_TOKEN = "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"
# GITHUB_API_URL = "https://api.github.com/orgs/Akindu-ID/repos"

class RepoRequest(BaseModel): 
    # General
    email: str
    functional_head_email: str
    requirement: str
    copy_emails: str
    # Data required for repo creation process
    repo_name: str
    organization: str
    repo_type: bool #false - public, true - private
    description: str
    teams: list
    pr_protection: bool
    enable_issues: bool
    website_url: str
    topics: list 
    cicd_requirement: str
    # DevOps
    job_type: str #= None
    group_id: str #= None
    devops_org: str #= None
    devops_project: str #= None

# Helper functions
def read_requests():
    try:
        with open(REQUESTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_requests(data):
    with open(REQUESTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Endpoints
@app.post("/create_request")
def create_request(repo: RepoRequest):
    new_request = repo.dict()
    new_request["timestamp"] = datetime.now().isoformat()
    new_request["approval_state"] = "Pending"
    requests_list = read_requests()
    requests_list.append(new_request)
    write_requests(requests_list)
    return {"message": "Repository request created successfully!", "request": new_request}

@app.get("/requests")
def get_requests():
    return read_requests()

@app.post("/approve_request/{repo_name}")
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
                repo_type = request["repo_type"]
                description = request["description"]
                pr_protection = request["pr_protection"]
                enable_issues = request["enable_issues"]
                website_url = request["website_url"]
                topics = request["topics"]
                print(repo_name, organization, repo_type, description, pr_protection, enable_issues, website_url, topics)
                create_repo(organization, repo_name, description, repo_type, enable_issues, website_url, GITHUB_TOKEN)
                if request["topics"]:
                   print(topics)
                   add_topics(organization, repo_name, topics, GITHUB_TOKEN)
                add_labels(organization, repo_name, GITHUB_TOKEN)
                add_issue_template(organization, repo_name, GITHUB_TOKEN)
                add_pr_template(organization, repo_name, GITHUB_TOKEN)
                if pr_protection == "true":
                    add_branch_protection(organization, repo_name, GITHUB_TOKEN)
                else:
                    add_branch_protection_bal(organization, repo_name, GITHUB_TOKEN) 
                request["approval_state"] = "Approved"
                write_requests(requests_list)          
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Repository creation failed: {str(e)}")
            break
            
    if not request_exists:
        raise HTTPException(status_code=404, detail="Request not found")
