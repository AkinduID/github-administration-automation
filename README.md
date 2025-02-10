# GitHub Administration Automation
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white"/></a>
<a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white"/></a>
<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/VS%20Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white"/></a>
<a href="https://git-scm.com/"><img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white"/></a>
<a href="https://github.com/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white"/></a>

## Project Overview
This project automates the creation of repositories within different organizations, reducing manual effort and ensuring consistency. Currently, the following organizations are used for testing.
* [GitOpsLab-1](https://github.com/GitOpsLab-1)


## Workflow

### 1. User Inputs
Users provide the following details before initiating the repository creation process:

#### General Information
- **Email**
- **Functional Head Email**
- **Requirement**
- **CC Email List**

#### Repository Details
- **Repository Name**
- **Organization Name**
- **Repository Type (Public/Private)**
- **Description**
- **Enable Issues (Boolean)**
- **Website URL**
- **Topics**

#### Security Details
- **Team List**
- **PR Branch Protection (Enabled/Disabled)**

#### DevOps Integration
- **Jenkins**
- **Azure**
- **Not Applicable**

### 2. Approval Process
Once a request is submitted, an approval request is generated. The administrator reviews and approves the request before proceeding.

### 3. Repository Creation Process
Once approved, the following automated steps take place:
1. Retrieve the list of all teams in the organization (At the backend startup).
2. Obtain a **Fine-Grained Personal Access Token (PAT)** for organization access.
3. Create a new repository in the designated organization.
4. Add topics (optional).
5. Add predefined labels.
6. Add issue templates.
7. Add pull request templates.
8. Configure branch protection rules.
9. Set permissions for teams.

## Technologies Used
- **Python** (for rapid prototyping)
- **FastAPI** (backend)
- **Streamlit** (frontend)
- **GitHub API** (for automation)

## Access Requirements
A **Fine-Grained Personal Access Token (PAT)** is required to interact with the GitHub API. The following permissions must be granted:

### Repository Permissions
- **Administration: Read & Write** → Required for repository creation and topic management.
- **Content: Read & Write** → Needed to add issue templates and pull request templates.
- **Pull Requests: Read & Write** → Required to add labels.

### Organization Permissions
- **Members: Read Only** → Required to fetch the list of teams within the organization.

---
This project simplifies and automates GitHub repository management, making it easier for teams to create and maintain repositories efficiently.
