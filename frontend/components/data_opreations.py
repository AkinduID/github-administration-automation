import requests
import streamlit as st

def create_request(api_url, request_data):
    try:
        response = requests.post(f"{api_url}/create_request", json=request_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating request: {e}")  # Handle errors in component
        return None  # Or return appropriate error indicator
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

def get_teams(api_url, organization):
    try:
        response = requests.get(f"{api_url}/get_teams/{organization}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error getting teams: {e}")
        return
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return

def get_all_requests(api_url):
    try:
        response = requests.get(f"{api_url}/requests")  # Or your specific endpoint
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching requests: {e}") # Show more informative error
        return None # Indicate failure
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

    #... other data handling functions

import requests
import streamlit as st

def get_user_requests(api_url, user_id):
    try:
        response = requests.get(f"{api_url}/requests/")  # Or your specific endpoint
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user requests: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

#... (Other functions in data_opreations.py)...


#... (Add other API interaction functions as needed: get_requests, approve_request, etc.)