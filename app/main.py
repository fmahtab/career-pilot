from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers.applications import router as application_router
from app.routers.auth import router as auth_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(application_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "AI Job Tracker API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/jobs/{job_id}")
def get_job(job_id: int):
    return {
        "job_id": job_id,
        "title": "Backend Developer"
    }


@app.get("/interviews/{interview_id}")
def get_interviews(interview_id: int):
    return{
        "interview_id": interview_id,
        "title": "Interview Ids"
    }

@app.get("/jobs")
def get_jobs(status: str = None):
    return{
        "message": "Job list fetched",
        "status_filter": status
    }



   