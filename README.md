# github-administration-automation

This Repo contains source code for the githib administration automation project.


# Project Details
This project aims to automate the repository creation process across different organizations.

Currently The Organization https://github.com/Akindu-ID/ is used to test the project

# Current Workflow

## 1. User Inputs
### general
* Email
* Functional head email
* Requirementmail 
* cc list
### Required for repo creation
* repo name
* oraganization
* repo type boolean
* description
* team list
* pr branch protection
* enable issues boolean
* website url
* topics
### DevOps
* Jenkins
* Azure
* Not Applicable


### Approve Request is Created. Admin reviews and Approves Request

## 4. Repo Creation Process

* List all teams in the organization (Run Once)

* Get PAT for Org

* Create a new repository in the organization (ask how it works when multiple teams are involved)

* Add Topics (Optional)

* Add Labels

* Add Issue Template if Issues are enabled

* Add PR Template

* Add Branch Protection Rules

* Set Infra Team Permissions


# Current Technologies
* Python (for rapid prototyping)
* FastAPI for Backend
* Streamlit for Frontend
* GitHub API