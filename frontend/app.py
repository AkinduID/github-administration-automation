import streamlit as st

st.title("Welcome to GitHub Repo Requests")
st.write("Please select your role:")  # More descriptive message

st.page_link("pages/user_dashboard.py", label="User", icon="1️⃣")
st.page_link("pages/admin_dashboard.py", label="Admin", icon="2️⃣")

# Optional: Add a message or instructions below the buttons
# st.write("Click 'User' to access the user dashboard or 'Admin' to access the admin dashboard.")