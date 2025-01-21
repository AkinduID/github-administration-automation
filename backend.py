from fastapi import FastAPI
from pydantic import BaseModel
import requests

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
    job_type: str = None
    group_id: str = None
    devops_org: str = None
    devops_project: str = None

@app.post("/create_repo")
def create_repo(repo: RepoRequest):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    payload = {
        "name": repo.repo_name,
        "description": repo.description,
        "private": True if repo.repo_type == "Private" else False,
    }

    # Create repository on GitHub
    response = requests.post(GITHUB_API_URL, json=payload, headers=headers)

    if response.status_code == 201:
        # Successfully created the GitHub repository, now handle CICD setup if applicable
        cicd_info = {
            "cicd_requirement": repo.cicd_requirement,
            "job_type": repo.job_type,
            "group_id": repo.group_id,
            "devops_org": repo.devops_org,
            "devops_project": repo.devops_project,
        }

        # This is where you could handle additional actions, e.g., setting up Jenkins or Azure Pipeline
        # For now, we're just returning the CICD-related information
        return {
            "message": f"Repository '{repo.repo_name}' created successfully!",
            "cicd_info": cicd_info
        }
    else:
        return {"error": response.json()}

# To run the FastAPI app:
# uvicorn backend:app --reload
