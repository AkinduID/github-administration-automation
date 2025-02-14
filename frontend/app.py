import streamlit as st

# Page Description: Entry Point for frontend

# ToDo 
# intregrate asgardeo authentication

st.title("Welcome to GitHub Repo Requests")
st.write("Please select your role:") 

st.page_link("pages/user_dashboard.py", label="User", icon="1️⃣")
st.page_link("pages/admin_dashboard.py", label="Admin", icon="2️⃣")