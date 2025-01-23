from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from datetime import datetime
import json

REQUESTS_FILE = "repo_requests.json"

# Create FastAPI instance
app = FastAPI()

# GitHub personal access token (replace with your actual token)
GITHUB_TOKEN = "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"
GITHUB_API_URL = "https://api.github.com/orgs/Akindu-ID/repos"

# Define the request model for creating repositories
class RepoRequest(BaseModel): 
    email: str
    functional_head_email: str
    requirement: str
    copy_emails: str
    repo_name: str
    organization: str
    repo_type: str
    description: str
    teams: list
    pr_protection: str
    enable_issues: str
    website_url: str
    topics: str
    cicd_requirement: str
    job_type: str #= None
    group_id: str #= None
    devops_org: str #= None
    devops_project: str #= None

def read_requests():
    try:
        with open(REQUESTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_requests(data):
    with open(REQUESTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.post("/create_request")
def create_request(repo: RepoRequest):
    # Add timestamp and initial approval state
    new_request = repo.dict()
    new_request["timestamp"] = datetime.now().isoformat()
    new_request["approval_state"] = "Pending"

    # Save the request to the JSON file
    requests_list = read_requests()
    requests_list.append(new_request)
    write_requests(requests_list)

    return {"message": "Repository request created successfully!", "request": new_request}

@app.get("/requests")
def get_requests():
    return read_requests()

@app.post("/approve_request/{repo_name}")
def approve_request(repo_name: str):
    # Read the requests from the JSON file
    requests_list = read_requests()
    for request in requests_list:
        if request["repo_name"] == repo_name:
            if request["approval_state"] != "Pending":
                raise HTTPException(status_code=400, detail="Request is already processed")

            # Update the approval state
            request["approval_state"] = "Approved"
            write_requests(requests_list)

            # Prepare payload for GitHub repository creation
            headers = {"Authorization": f"token {GITHUB_TOKEN}"}
            payload = {
                "name": request["repo_name"],
                "description": request["description"],
                "private": True if request["repo_type"] == "Private" else False,
                "homepage": request["website_url"] if request["website_url"] else None,
                "topics": request["topics"].split(",") if request["topics"] else [],
                "has_issues": True if request["enable_issues"] == "Yes" else False,
            }

            # Send API request to create the GitHub repository
            response = requests.post(GITHUB_API_URL, json=payload, headers=headers)

            if response.status_code == 201:
                # After repository is created, handle PR protection
                repo_url = response.json().get('url')  # Get the repo URL to set branch protection
                if request["pr_protection"]:
                    # Call GitHub API to set branch protection based on request['pr_protection']
                    protection_payload = {
                        "required_status_checks": {"strict": True, "contexts": []},
                        "enforce_admins": False,
                        "required_pull_request_reviews": {"dismiss_stale_reviews": True, "require_code_owner_reviews": False},
                        "restrictions": None
                    }
                    protection_url = f"{repo_url}/branches/main/protection"
                    protection_response = requests.put(protection_url, json=protection_payload, headers=headers)
                    
                    if protection_response.status_code != 200:
                        return {"error": f"Failed to apply branch protection: {protection_response.json()}"}

                return {"message": f"Repository '{repo_name}' approved and created successfully!"}
            else:
                # Roll back approval if GitHub creation fails
                request["approval_state"] = "Pending"
                write_requests(requests_list)
                return {"error": response.json()}

    raise HTTPException(status_code=404, detail="Request not found")
