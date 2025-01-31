# app/models/repo.py
from pydantic import BaseModel
from typing import List

class RepoRequest(BaseModel):
    # General information
    email: str
    functional_head_email: str
    requirement: str
    copy_emails: str
    
    # Data for repo creation
    repo_name: str
    organization: str
    repo_type: bool  # False for public, True for private
    description: str
    teams: list
    pr_protection: bool
    enable_issues: bool
    website_url: str
    topics: List[str]
    cicd_requirement: str
    
    # DevOps info
    job_type: str
    group_id: str
    devops_org: str
    devops_project: str
