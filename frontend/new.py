import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"
CREATE_REQUEST_URL = f"{FASTAPI_URL}/create_request"
GET_REQUESTS_URL = f"{FASTAPI_URL}/requests"
APPROVE_REQUEST_URL = f"{FASTAPI_URL}/approve_request"
GET_TEAMS_URL = f"{FASTAPI_URL}/get_teams"

teams=[]

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Function to go to the next step
def next_step():
    if st.session_state.step==1:
        if st.session_state.form_data.get('email', "") == "" or st.session_state.form_data.get('lead_email', "") == "" or st.session_state.form_data.get('requirement', "") == "" or st.session_state.form_data.get('cc_list', "") == "":
            st.error("Please fill all the required fields.")
            return
    if st.session_state.step==2:
        if st.session_state.form_data.get('repo_name', "") == "" or st.session_state.form_data.get('organization', "") == "" or st.session_state.form_data.get('repo_type', "") == "" or st.session_state.form_data.get('description', "") == "" or st.session_state.form_data.get('enable_issues', "") == "":
            st.error("Please fill all the required fields.")
            return
    if st.session_state.step==3:
        if st.session_state.form_data.get('pr_protection', "") == "" or st.session_state.form_data.get('teams', "") == []:
            st.error("Please fill all the required fields.")
            return
    if st.session_state.step==4:
        if st.session_state.form_data.get('cicd_requirement', "") == "":
            st.error("Please fill all the required fields.")
            return
    if st.session_state.step==5:
        if st.session_state.form_data.get('cicd_requirement', "") == "Jenkins Job":
            if st.session_state.form_data.get('jenkins_job_type', "") == "" or st.session_state.form_data.get('jenkins_group_id', "") == "":
                st.error("Please fill all the required fields.")
                return
        elif st.session_state.form_data.get('cicd_requirement', "") == "Azure Pipeline":
            if st.session_state.form_data.get('azure_devops_org', "") == "" or st.session_state.form_data.get('azure_devops_project', "") == "":
                st.error("Please fill all the required fields.")
                return
    st.session_state.step += 1

# Function to go to the previous step
def prev_step():
    st.session_state.step -= 1

# Function to submit the form
def submit_form():
    st.success("Form submitted successfully!")
    st.write("Form Data:", st.session_state.form_data)
    st.session_state.form_data["repo_type"] = True if st.session_state.form_data["repo_type"] == "Private" else False
    st.session_state.form_data["enable_issues"] = True if st.session_state.form_data["enable_issues"] == "Yes" else False
    st.session_state.form_data["pr_protection"] = True if st.session_state.form_data["pr_protection"] == "Default Branch protection Rules" else False
    st.session_state.form_data["topics"] = st.session_state.form_data["topics"].split(",") if st.session_state.form_data["topics"] else []
    st.session_state.form_data["enable_triage_wso2all"] = True if st.session_state.form_data["enable_triage_wso2all"] == "Yes" else False
    st.session_state.form_data["enable_triage_wso2allinterns"] = True if st.session_state.form_data["enable_triage_wso2allinterns"] == "Yes" else False
    payload = st.session_state.form_data
    print(payload)
    response = requests.post(CREATE_REQUEST_URL, json=payload)
    if response.status_code == 200:
        st.success(response.json().get("message", "Repository request created successfully"))
    else:
        st.error(f"Error: {response.json().get('error', 'Unknown error')}")

# Progress bar
progress = st.progress((st.session_state.step - 1) / 6)

# Step 1: General Information
if st.session_state.step == 1:
    st.header("Step 1: General Information")
    st.session_state.form_data['email'] = st.text_input("Email *", value=st.session_state.form_data.get('email',""), key="email")
    functional_heads_list = [
            "Integration", "Identity Access Management / Asgardeo", "Open Banking", "Choreo",
            "Ballerina", "Solutions Architecture"
        ]
    st.session_state.form_data['lead_email'] = st.selectbox('Functional Head Email *', functional_heads_list,index=functional_heads_list.index(st.session_state.form_data.get('lead_email', functional_heads_list[0])),key="lead_email")
    st.session_state.form_data['requirement'] = st.text_area("Requirement *", value = st.session_state.form_data.get("requirement",""),key="requirement" ,help="Purpose of requesting this repo")
    st.session_state.form_data['cc_list'] = st.text_input("Copy this email *",value=st.session_state.form_data.get('cc_list', ""), key="cc_list", help="Comma separated list of emails/groups to inform")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Next", on_click=next_step)

# Step 2: Repository Information
elif st.session_state.step == 2:
    st.header("Step 2: Repository Information")
    st.session_state.form_data['repo_name'] = st.text_input("Repo Name *",value=st.session_state.form_data.get('repo_name', ""), key="repo_name" ,help="Help on repository naming conventions")
    # org_options = [
        #     "wso2", "wso2-extensions", "wso2-incubator", 
        #     "ballerina-platform", "ballerina-guides", 
        #     "wso2-enterprise", "asgardeo", "choreo-test-apps", "asgardeo-samples", "Other"
        # ]
    org_options = [
            "gitopslab", "gitopslab-enterprise", "gitopslab-extensions", "GitOpsLab-4", "GitOpsLab-5","wso2-enterprise","wso2-incubator"
        ]
    st.session_state.form_data['organization'] = st.selectbox("Organization *", org_options, index=org_options.index(st.session_state.form_data.get('organization', org_options[0])),
    key="organization")
    st.session_state.form_data['repo_type'] = st.radio("Repo Type *", options=["Public", "Private"],index=["Public", "Private"].index(st.session_state.form_data.get('repo_type', "Public")),
    key="repo_type")
    st.session_state.form_data['description'] = st.text_area("Description *", value = st.session_state.form_data.get("description",""),key="description" ,help="Short description to add to the repository's ABOUT section in GitHub")
        # teams = st.multiselect(
        #     "Team *", 
        #     options=["Analytics", "APIM", "Ballerina", "Cellery", "Choreo", "Financial Solutions", "IAM", "Integration", "SRE / WUM", "Other"]
        # )
    st.session_state.form_data['enable_issues'] = st.radio("Enable 'Issues' *", options=["Yes", "No"],index=["Yes", "No"].index(st.session_state.form_data.get('enable_issues', "Yes")),key="enable_issues")
    st.session_state.form_data['website_url'] = st.text_input("Website URL", value = st.session_state.form_data.get("website_url",""),key="website_url",help="Provide an URL with more information about the repository")
    st.session_state.form_data['topics'] = st.text_input("Topics", value = st.session_state.form_data.get("topics",""),key="topics", help="List topics to classify the repo")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

# Step 3: Security Information
elif st.session_state.step == 3 and st.session_state.form_data['organization'] != "gitopslab-enterprise":
    teams = requests.get(f"{GET_TEAMS_URL}/{st.session_state.form_data['organization']}").json()
    print(teams)
    st.header("Step 3: Security Information")
    pr_protection_options = ["Default Branch Protection Rules", "'Ballerina Library' Repo Branch Protection Rules"]
    pr_protection_default_value = st.session_state.form_data.get("pr_protection", "Default Branch Protection Rules")
    if pr_protection_default_value not in pr_protection_options:
        default_value = "Default Branch Protection Rules"
    st.session_state.form_data['pr_protection'] = st.radio(
        "Add PR branch protection *",
        options=pr_protection_options,
        index=pr_protection_options.index(pr_protection_default_value),  # Set the correct index
        key="pr_protection",
        help="Select the type of branch protection required")
    # st.session_state.form_data['pr_protection'] = st.radio("Add PR branch protection *", options=["Default Branch Protection Rules", "'Ballerina Library' Repo Branch Protection Rules"],index=["Default Branch Protection Rules", "'Ballerina Library' Repo Branch Protection Rules"].index(st.session_state.form_data.get("pr_protection", "Default Branch Protection Rules")),key="pr_protection",help="Select the type of branch protection required")
    st.session_state.form_data['teams'] = st.multiselect("Team *", options=teams,key="teams")
    st.session_state.form_data['enable_triage_wso2all']=""
    st.session_state.form_data['enable_triage_wso2allinterns']=""
    st.session_state.form_data['disable_triage_reason']=""
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

elif st.session_state.step == 3 and st.session_state.form_data['organization'] == "gitopslab-enterprise":
    st.header("Step 3: Security Information")
    teams = requests.get(f"{GET_TEAMS_URL}/{st.session_state.form_data['organization']}").json()
    print(teams)
    st.session_state.form_data['pr_protection'] = st.radio("Add PR branch protection *", options=["Default Branch Protection Rules", "'Ballerina Library' Repo Branch Protection Rules"],index=["Default Branch Protection Rules", "'Ballerina Library' Repo Branch Protection Rules"].index(st.session_state.form_data.get("pr_protection", "Default Branch Protection Rules")),key="pr_protection",help="Select the type of branch protection required")
    st.session_state.form_data['teams'] = st.multiselect("Team *", options=teams,key="teams")
    st.session_state.form_data['enable_triage_wso2all']=st.radio("Enable Triage acces to wso2 all group",options=["Yes","No"])
    st.session_state.form_data['enable_triage_wso2allinterns']=st.radio("Enable Triage acces to wso2 all interns group",options=["Yes","No"])
    st.session_state.form_data['disable_triage_reason']=st.text_input("Please explain why we should NOT grant readonly access to all wso2 employees / interns",value=st.session_state.form_data.get('disable_triage_reason', ""), key="disable_triage_reason",help=" If 'NO' is selected for either one of the above questions, please give reason for selections.")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

# Step 4
elif st.session_state.step == 4:
    st.header("Step 4: CI/CD Configurations")
    st.session_state.form_data['cicd_requirement'] = st.radio(
            "CICD requirement", 
            options=["Jenkins Job", "Azure Pipeline", "Not Applicable"],
            help="Teams can opt for a Jenkins job to deploy to nexus or an Azure pipeline to deploy to Azure.",
            index=["Jenkins Job", "Azure Pipeline", "Not Applicable"].index(st.session_state.form_data.get('cicd_requirement', "Jenkins Job")),
            key='cicd_requirement'
        )
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

# Step 4.1: Jenkins 
elif st.session_state.step == 5 and st.session_state.form_data['cicd_requirement']=="Jenkins Job":
    st.header("Step 4: Jenkins Configurations")
    options = ["product-*", "carbon-*", "identity-*", "apim-*", "esb-*", "Other:"]
    default_value = st.session_state.form_data.get("jenkins_job_type", "product-*")

# Ensure the default value exists in the options
    if default_value not in options:
        default_value = "product-*"
    st.session_state.form_data['jenkins_job_type'] = st.selectbox(
        "Job Type *",
        options=options,
        index=options.index(default_value),  # Set the correct index
        key="jenkins_job_type"
    )
    st.session_state.form_data['jenkins_group_id'] = st.text_input("Group ID", help="Enter the Group ID for the Jenkins job", value = st.session_state.form_data.get("jenkins_group_id",""),key="jenkins_group_id")
    st.session_state.form_data['azure_devops_org'] = ""
    st.session_state.form_data['azure_devops_project'] = ""
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

# Step 5.1: Azure
elif st.session_state.step == 5 and st.session_state.form_data['cicd_requirement']=="Azure Pipeline":
    st.header("Step 4: Jenkins Configurations")
    st.session_state.form_data['jenkins_job_type'] = ""
    st.session_state.form_data['jenkins_group_id'] = ""
    st.session_state.form_data['azure_devops_org'] = st.text_input("DevOps Organization *", help="State the DevOps Organization name in Azure",value = st.session_state.form_data.get("azure_devops_org",""),key="azure_devops_org")
    st.session_state.form_data['azure_devops_project'] = st.text_input("DevOps Project *", help="State the DevOps project name in Azure", value = st.session_state.form_data.get("azure_devops_project",""),key="azure_devops_project")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Next", on_click=next_step)

# Step 6: Review and submit
elif st.session_state.step == 6 or (st.session_state.step==5 and st.session_state.form_data['cicd_requirement']=="Not Applicable"):
    if st.session_state.form_data['cicd_requirement']=="Not Applicable":
        st.session_state.form_data['jenkins_job_type'] = ""
        st.session_state.form_data['jenkins_group_id'] = ""
        st.session_state.form_data['azure_devops_org'] = ""
        st.session_state.form_data['azure_devops_project'] = ""
    st.header("Step 5: Review and Submit")
    st.write("Please review your information:")
    st.write(st.session_state.form_data)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Back", on_click=prev_step)
    with col2:
        st.button("Submit", on_click=submit_form)

# Update progress bar
progress.progress(st.session_state.step / 6)