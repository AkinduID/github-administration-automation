# backend.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from datetime import datetime
import json

# Create FastAPI instance
app = FastAPI()

REQUESTS_FILE = "repo_requests.json"
GITHUB_TOKEN = "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"
GITHUB_API_URL = "https://api.github.com/orgs/Akindu-ID/repos"

class RepoRequest(BaseModel):
    name: str
    description: str
    private: bool

def read_requests():
    try:
        with open(REQUESTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_requests(data):
    with open(REQUESTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.post("/create_request")
def create_request(repo: RepoRequest):
    # Add timestamp and initial approval state
    new_request = repo.dict()
    new_request["timestamp"] = datetime.now().isoformat()
    new_request["approval_state"] = "Pending"

    # Save the request to the JSON file
    requests_list = read_requests()
    requests_list.append(new_request)
    write_requests(requests_list)

    return {"message": "Repository request created successfully!", "request": new_request}


@app.get("/requests")
def get_requests():
    return read_requests()

@app.post("/approve_request/{name}")
def approve_request(name: str):
    # Read the requests from the JSON file
    requests_list = read_requests()
    for request in requests_list:
        if request["name"] == name:
            if request["approval_state"] != "Pending":
                raise HTTPException(status_code=400, detail="Request is already processed")

            # Update the approval state
            request["approval_state"] = "Approved"
            write_requests(requests_list)

            # Trigger GitHub repository creation
            headers = {"Authorization": f"token {GITHUB_TOKEN}"}
            payload = {
                "name": request["name"],
                "description": request["description"],
                "private": True if request["private"] == True else False,
            }

            response = requests.post(GITHUB_API_URL, json=payload, headers=headers)

            if response.status_code == 201:
                return {"message": f"Repository '{name}' approved and created successfully!"}
            else:
                # Roll back approval if GitHub creation fails
                request["approval_state"] = "Pending"
                write_requests(requests_list)
                return {"error": response.json()}

    raise HTTPException(status_code=404, detail="Request not found")

# To run the FastAPI app:
# uvicorn backend:app --reload
