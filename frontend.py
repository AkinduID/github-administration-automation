# frontend.py
import streamlit as st
import requests

# FastAPI URL for creating repositories
FASTAPI_URL = "http://127.0.0.1:8000/create_repo"  # Replace with actual backend URL if deployed

st.title("New Github Repository Request")
with st.form(key='new_repo_form'):

    email = st.text_input("Email *", value="akindu@wso2.com")
    functional_heads_list = [
        "Integration",
        "Identity Access Management / Asgardeo",
        "Open Banking",
        "Choreo",
        "Ballerina",
        "Solutions Architecture"]
    functional_head_email = st.selectbox('Functional Head:',functional_heads_list)
    requirement = st.text_area("Requirement *", help="Purpose of requesting this repo")
    copy_emails = st.text_input("Copy this email *", help="Comma separated list of emails/groups to inform")
    repo_name = st.text_input("Repo Name *", help="Help on repository naming conventions")
    org_options = [
        "wso2", "wso2-support", "wso2-extensions", "wso2-incubator", 
        "ballerina-platform", "ballerina-guides", "wso2-cellery", "siddhi-io", 
        "wso2-enterprise", "asgardeo", "choreo-test-apps", "asgardeo-samples", "Other"
    ]
    org = st.selectbox("Organization *", org_options)
    repo_type = st.radio("Repo Type *", options=["Public", "Private"])
    description = st.text_area("Description *", help="Short description to add to the repository's ABOUT section in GitHub")
    teams = st.multiselect(
        "Team *", 
        options=["Analytics", "APIM", "Ballerina", "Cellery", "Choreo", "Financial Solutions", "IAM", "Integration", "SRE / WUM", "Other"]
    )
    pr_protection = st.radio("Add PR branch protection *", options=["Default Branch protection Rules", "'Ballerina Library' Repo Branch Protection Rules"],help="Select the type of branch protection required")
    enable_issues = st.radio("Enable 'Issues' *", options=["Yes", "No"])
    website_url = st.text_input("Website URL", help="Provide an URL with more information about the repository")
    topics = st.text_input("Topics", help="List topics to classify the repo")
   
    cicd_requirement = st.radio(
        "CICD requirement", 
        options=["Jenkins Job", "Azure Pipeline", "Not Applicable"],
        help="Teams can opt for a Jenkins job to deploy to nexus or an Azure pipeline to deploy to Azure.",
        key='cicd_requirement'
    )

    st.subheader("Jenkins Job Configuration")
    job_type = st.selectbox("Job Type *", options=["product-*", "carbon-*", "identity-*", "apim-*", "esb-*", "Other:"])
    group_id = st.text_input("Group ID", help="Enter the Group ID for the Jenkins job")

    st.subheader("Azure Pipeline Configuration")
    devops_org = st.text_input("DevOps Organization *", help="State the DevOps Organization name in Azure")
    devops_project = st.text_input("DevOps Project *", help="State the DevOps project name in Azure")

    submit_button = st.form_submit_button(label="Submit Request")


if submit_button:
    # Check if required fields are filled
    if repo_name and description and functional_head_email and org:
        payload = {
            "email": email,
            "functional_head_email": functional_head_email,
            "requirement": requirement,
            "copy_emails": copy_emails,
            "repo_name": repo_name,
            "organization": org,
            "repo_type": repo_type,
            "description": description,
            "teams": teams,
            "pr_protection": pr_protection,
            "enable_issues": enable_issues,
            "website_url": website_url,
            "topics": topics,
            "cicd_requirement": cicd_requirement,
            "job_type": job_type if cicd_requirement == "Jenkins Job" else None,
            "group_id": group_id if cicd_requirement == "Jenkins Job" else None,
            "devops_org": devops_org if cicd_requirement == "Azure Pipeline" else None,
            "devops_project": devops_project if cicd_requirement == "Azure Pipeline" else None
        }

        # Send request to FastAPI backend
        response = requests.post(FASTAPI_URL, json=payload)

        if response.status_code == 200:
            st.success(response.json().get("message", "Repository request created successfully"))
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.error("Please fill out all required fields.")