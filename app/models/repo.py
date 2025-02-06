# app/models/repo.py
from pydantic import BaseModel
from typing import List

class RepoRequest(BaseModel):
    # General information
    email: str
    lead_email: str
    requirement: str
    cc_list: str
    
    # Data for repo creation
    repo_name: str
    organization: str
    repo_type: bool  # False for public, True for private
    description: str
    enable_issues: bool
    website_url: str
    topics: List[str]

    #Security
    pr_protection: bool
    teams: list
    enable_triage_wso2all: bool
    enable_triage_wso2allinterns: bool
    disable_triage_reason: str
   
    # CI/CD config
    cicd_requirement: str
    
    # Jenkins Job Configuration
    jenkins_job_type: str
    jenkins_group_id: str

    # Azure Pipeline Configuration
    azure_devops_org: str
    azure_devops_project: str
