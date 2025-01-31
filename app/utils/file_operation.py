# app/utils/file_operations.py
import json
from typing import Any

REQUESTS_FILE = "repo_requests.json"

def read_requests() -> list:
    """Reads the repository requests from the JSON file."""
    try:
        with open(REQUESTS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_requests(data: Any):
    """Writes the repository requests to the JSON file."""
    with open(REQUESTS_FILE, "w") as f:
        json.dump(data, f, indent=4)
