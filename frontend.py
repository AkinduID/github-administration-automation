import streamlit as st
import requests

# ToDo
# format the inpout data in payload to match the backend model
# add the demo data and change the frontend

FASTAPI_URL = "http://127.0.0.1:8000"
CREATE_REQUEST_URL = f"{FASTAPI_URL}/create_request"
GET_REQUESTS_URL = f"{FASTAPI_URL}/requests"
APPROVE_REQUEST_URL = f"{FASTAPI_URL}/approve_request"

if "current_page" not in st.session_state:
    st.session_state.current_page = "Normal Page"

if st.sidebar.button("Normal Page"):
    st.session_state.current_page = "Normal Page"
if st.sidebar.button("Admin Page"):
    st.session_state.current_page = "Admin Page"

if st.session_state.current_page == "Normal Page":
    st.title("New Github Repository Request")

    with st.form(key='new_repo_form'):
        email = st.text_input("Email *", value="akindu@wso2.com")
        functional_heads_list = [
            "Integration", "Identity Access Management / Asgardeo", "Open Banking", "Choreo",
            "Ballerina", "Solutions Architecture"
        ]
        functional_head_email = st.selectbox('Functional Head:', functional_heads_list)
        requirement = st.text_area("Requirement *", help="Purpose of requesting this repo")
        copy_emails = st.text_input("Copy this email *", help="Comma separated list of emails/groups to inform")
        repo_name = st.text_input("Repo Name *", help="Help on repository naming conventions")
        # org_options = [
        #     "wso2", "wso2-support", "wso2-extensions", "wso2-incubator", 
        #     "ballerina-platform", "ballerina-guides", "wso2-cellery", "siddhi-io", 
        #     "wso2-enterprise", "asgardeo", "choreo-test-apps", "asgardeo-samples", "Other"
        # ]
        org_options = [
            "GitOpsLabs-1", "GitOpsLabs-2", "GitOpsLabs-3", "GitOpsLabs-4", "GitOpsLabs-5"
        ]
        org = st.selectbox("Organization *", org_options)
        repo_type_input = st.radio("Repo Type *", options=["Public", "Private"])
        description = st.text_area("Description *", help="Short description to add to the repository's ABOUT section in GitHub")
        # teams = st.multiselect(
        #     "Team *", 
        #     options=["Analytics", "APIM", "Ballerina", "Cellery", "Choreo", "Financial Solutions", "IAM", "Integration", "SRE / WUM", "Other"]
        # )
        teams = st.multiselect(
            "Team *", 
            options=["GitOPsLabs 1 Team 1", "GitOpsLabs 1 Team 2", "GitOpsLabs 1 Team 3", 
                     "GitOpsLabs 2 Team 1", "GitOpsLabs 2 Team 2", "GitOpsLabs 2 Team 3", 
                     "GitOpsLabs 3 Team 1", "GitOpsLabs 3 Team 2", "GitOpsLabs 3 Team 3",
                     "GitOpsLabs 4 Team 1", "GitOpsLabs 4 Team 2", "GitOpsLabs 4 Team 3",
                     "GitOpsLabs 5 Team 1", "GitOpsLabs 5 Team 2", "GitOpsLabs 5 Team 3"]
        )
        pr_protection_input = st.radio("Add PR branch protection *", options=["Default Branch protection Rules", "'Ballerina Library' Repo Branch Protection Rules"], help="Select the type of branch protection required")
        enable_issues_input = st.radio("Enable 'Issues' *", options=["Yes", "No"])
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
        if repo_name and description and functional_head_email and org:
            repo_type = True if repo_type_input == "Private" else False
            pr_protection = True if pr_protection_input == "Default Branch protection Rules" else False
            enable_issues = True if enable_issues_input == "Yes" else False
            payload = {
                "email": email,
                "functional_head_email": functional_head_email,
                "requirement": requirement,
                "copy_emails": copy_emails,
                "repo_name": repo_name,
                "organization": org,
                "repo_type": repo_type, #true if "Private" false if "Public", bool
                "description": description,
                "teams": teams,
                "pr_protection": pr_protection, #true if "Default Branch protection Rules" false if "Ballerina Library Repo Branch Protection Rules", bool
                "enable_issues": enable_issues, #true if "Yes" false if "No", bool
                "website_url": website_url,
                "topics": topics.split(",") if topics else [],
                "cicd_requirement": cicd_requirement,
                "job_type": job_type, #if cicd_requirement == "Jenkins Job" else None,
                "group_id": group_id, #if cicd_requirement == "Jenkins Job" else None,
                "devops_org": devops_org, #if cicd_requirement == "Azure Pipeline" else None,
                "devops_project": devops_project #if cicd_requirement == "Azure Pipeline" else None
            }
            print(payload)
            # Send request to FastAPI backend
            response = requests.post(CREATE_REQUEST_URL, json=payload)

            if response.status_code == 200:
                st.success(response.json().get("message", "Repository request created successfully"))
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        else:
            st.error("Please fill out all required fields.")

# Admin Page
elif st.session_state.current_page == "Admin Page":
    st.title("Admin Page")
    st.write("View and approve requests.")

    response = requests.get(GET_REQUESTS_URL)
    if response.status_code == 200:
        requests_list = response.json()
        for req in requests_list:
            st.write(f"### {req['repo_name']}")
            st.write(f"Email: {req['email']}")
            st.write(f"Requirement: {req['requirement']}")
            st.write(f"Timestamp: {req['timestamp']}")
            st.write(f"Approval State: {req['approval_state']}")
            if req["approval_state"] == "Pending":
                if st.button(f"Approve {req['repo_name']}",key=f"approve_{req['timestamp']}"):
                    approve_response = requests.post(f"{APPROVE_REQUEST_URL}/{req['repo_name']}")
                    if approve_response.status_code == 200:
                        st.success(f"Request for {req['repo_name']} approved!")
                        st.rerun()
                    else:
                        st.error(f"Failed to approve {req['repo_name']}.")
            st.markdown("---")  # Horizontal line separator
    else:
        st.error("Failed to fetch requests.")

