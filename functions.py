from tasks.list_teams import list_teams
from tasks.get_pat import get_pat
from tasks.create_repo import create_repo
from tasks.add_topics import add_topics
from tasks.add_labels import add_labels
from tasks.add_issue_template import add_issue_template
from tasks.add_pr_template import add_pr_template
from tasks.add_branch_protection import add_branch_protection
from tasks.add_branch_protection_bal import add_branch_protection_bal
from tasks.set_team_permissions import set_team_permissions
from tasks.get_pat import get_pat


# Export all functions in a single namespace
__all__ = ["list_teams","get_pat", "create_repo", "add_topics","add_labels","add_issue_template","add_pr_template","add_branch_protection","add_branch_protection_bal","set_team_permissions","get_pat"]


# Repo Creation Flow

# 1. List all teams in the organization (Run Once) (can be run after step 8)
# 2. Get PAT for org
# 3. Create a new repository in the organization 
# 4. Add Topics (Optional)
# 5. Add Labels
# 6. Add Issue Template
# 7. Add PR Template
# 8. Add Branch Protection Rules
# 9. Set Infra Team Permissions


# Approve Request Flow
# We need to add the following steps to the approve_request function in backend.py
# pseduo code
# def approve_request(repo_name: str):
#     requests_list = read_requests()
#     for request in requests_list:
#         if request["repo_name"] == repo_name:
#             if request["approval_state"] != "Pending":
#                 raise HTTPException(status_code=400, detail="Request is already processed")
#             request["approval_state"] = "Approved"
#             write_requests(requests_list)
#             create_repo()
#             if requests["topics"]:
#                   add_topics()
#             add_labels()
#             add_issue_template()
#             add_pr_template()
#             add_branch_protection()
#             set_infra_team_permissions()