import streamlit as st
import requests

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
        repo_name = st.text_input("Repository Name")
        repo_description = st.text_area("Repository Description")
        is_private = st.checkbox("Private Repository")
        submit_button = st.form_submit_button(label="Submit Request")

        if submit_button:
            if repo_name and repo_description:
                payload = {
                    "name": repo_name,
                    "description": repo_description,
                    "private": is_private
                }

                # Send request to FastAPI backend
                response = requests.post(CREATE_REQUEST_URL, json=payload)

                if response.status_code == 200:
                    st.success(response.json().get("message", "Repository request created successfully"))
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")
            else:
                st.error("Please fill out all required fields.")

elif st.session_state.current_page == "Admin Page":
    st.title("Admin Page")
    st.write("View and approve requests.")

    response = requests.get(GET_REQUESTS_URL)
    if response.status_code == 200:
        requests_list = response.json()
        for req in requests_list:
            st.write(f"Name: {req['name']}")
            st.write(f"Description: {req['description']}")
            st.write(f"Private: {req['private']}")
            st.write(f"Timestamp: {req['timestamp']}")
            st.write(f"Approval State: {req['approval_state']}")
            if req["approval_state"] == "Pending":
                if st.button(f"Approve {req['name']}", key=f"approve_{req['timestamp']}"):
                    approve_response = requests.post(f"{APPROVE_REQUEST_URL}/{req['name']}")
                    if approve_response.status_code == 200:
                        st.success(f"Request for {req['name']} approved!")
                        # Refresh the page to update the approval state
                        st.experimental_rerun()
                    else:
                        st.error(f"Failed to approve {req['name']}.")
            st.markdown("---")  # Horizontal line separator
    else:
        st.error("Failed to fetch requests.")
