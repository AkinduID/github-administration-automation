# app/main.py
from fastapi import FastAPI
from app.api.repo import router as repo_router

app = FastAPI()

app.include_router(repo_router)
