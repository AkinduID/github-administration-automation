from fastapi import FastAPI
from app.api.repo import router as repo_router
from app.tasks.github_operations import list_teams  # Import the function

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Running list_teams at startup...")
    list_teams()

app.include_router(repo_router)
