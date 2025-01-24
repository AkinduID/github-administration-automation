from tasks.list_teams import list_teams
from tasks.get_pat import get_pat
from tasks.create_repo import create_repo
from tasks.add_topics import add_topics
from tasks.add_labels import add_labels
from tasks.add_issue_template import add_issue_template
from tasks.add_pr_template import add_pr_template
from tasks.add_branch_protection import add_branch_protection


# Export all functions in a single namespace
__all__ = ["list_teams","get_pat", "create_repo", "add_topics","add_labels","add_issue_template","add_pr_template","add_branch_protection"]


# Repo Creation Flow

# 1. List all teams in the organization (Run Once)
# 2. Get PAT for Org
# 3. Create a new repository in the organization (ask how it works when multiple teams are involved)
# 4. Add Topics (Optional)
# 5. Add Labels
# 6. Add Issue Template if Issues are enabled
# 7. Add PR Template
# 8. Add Branch Protection Rules
# 9. Set Infra Team Permissions