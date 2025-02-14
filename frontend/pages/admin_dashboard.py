import streamlit as st
import requests
from components import data_opreations  # Import your data handling components
GET_REQUESTS_URL = "http://localhost:8000/requests"
APPROVE_REQUEST_URL = "http://localhost:8000/approve_request"

st.title("Admin Page")
st.write("View and approve requests.")

response = requests.get(GET_REQUESTS_URL)
if response.status_code == 200:
    requests_list = response.json()
    for req in requests_list:
        st.write(f"### {req['repo_name']}")
        # st.write(f"Email: {req['email']}")
        # st.write(f"Requirement: {req['requirement']}")
        st.write(f"Timestamp: {req['timestamp']}")
        st.write(f"Approval State: {req['approval_state']}")
        st.write(f"Organization: {req['organization']}")
        st.write(f"Repo Type: {'Private' if req['repo_type'] else 'Public'}")
        st.write(f"Description: {req['description']}")
        st.write(f"Teams: {req['teams']}")
        st.write(f"PR Protection: {'Default Branch protection Rules' if req['pr_protection'] else 'Ballerina Library Repo Branch Protection Rules'}")
        st.write(f"Enable Issues: {'Yes' if req['enable_issues'] else 'No'}")
        st.write(f"Website URL: {req['website_url']}")
        st.write(f"Topics: {req['topics']}")
        # st.write(f"CICD Requirement: {req['cicd_requirement']}")
        # st.write(f"Job Type: {req['job_type']}")
        # st.write(f"Group ID: {req['group_id']}")
        # st.write(f"DevOps Organization: {req['devops_org']}")
        # st.write(f"DevOps Project: {req['devops_project']}")
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