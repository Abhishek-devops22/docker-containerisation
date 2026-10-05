import os

from fastapi import FastAPI

app = FastAPI(title="Sample API")


@app.get("/")
def root():
    return {"message": "Hello from Docker!", "env": os.getenv("APP_ENV", "dev")}


@app.get("/health")
def health():
    return {"status": "ok"}
