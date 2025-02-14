import streamlit as st
from components import data_opreations  # Import your data handling components

api_url = "http://localhost:8000"  # Your API URL
st.title("User Dashboard")

user_id = True  # For testing purposes (replace with actual user ID retrieval)

if user_id:
    requests = data_opreations.get_user_requests(api_url, user_id)
    if requests:
        if not requests:  # More Pythonic way to check for empty list
            st.write("You haven't made any requests yet.")
        else:
            displayed_request_ids = set()  # Keep track of displayed IDs
            for request in requests:
                request_id = request.get('id')

                if request_id is not None and request_id not in displayed_request_ids:  # Check for None AND duplicates
                    displayed_request_ids.add(request_id)  # Add to the set of displayed IDs
                    st.write(f"**Request ID:** {request_id}")
                    st.write(f"**Project Name:** {request.get('repo_name')}")
                    st.write(f"**Status:** {request.get('status', 'Pending')}")
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button(f"Edit", key=f"edit_{request_id}"):
                            st.session_state.edit_request_id = request_id
                            st.rerun()  # Use st.rerun() for consistency
                    with col2:
                        if st.button(f"View", key=f"view_{request_id}"):
                            st.session_state.view_request_id = request_id
                            st.rerun()

                elif request_id is None:
                    st.write("Request ID is missing for this item.")
                elif request_id in displayed_request_ids:
                    st.write(f"Duplicate request id found: {request_id}. Please check data integrity.")


            if "edit_request_id" in st.session_state:
                edit_request_id = st.session_state.edit_request_id
                edit_request_data = data_opreations.get_request(api_url, edit_request_id)
                if edit_request_data:
                    from pages import new_request  # import the form page
                    edited_data = new_request.show_new_request_form(api_url, existing_data=edit_request_data)
                    if edited_data:
                        if data_opreations.update_request(api_url, edit_request_id, edited_data):
                            st.success("Request updated successfully!")
                            del st.session_state.edit_request_id
                            st.rerun()
                        else:
                            st.error("Failed to update the request.")
                else:
                    st.error("Could not retrieve request data for editing.")

            if "view_request_id" in st.session_state:
                view_request_id = st.session_state.view_request_id
                view_request_data = data_opreations.get_request(api_url, view_request_id)
                if view_request_data:
                    st.write("Request Details:")
                    st.write(view_request_data)
                    if st.button("Back to Dashboard"):
                        del st.session_state.view_request_id
                        st.rerun()
                else:
                    st.error("Could not retrieve request data for viewing.")

    else:
        st.error("Failed to fetch requests.")
else:
    st.error("User ID not found. Please log in.")

if st.button("Create New Request"):
    from pages import new_request  # import the form page
    new_request.show_new_request_form(api_url)  # Pass the api_url to the form