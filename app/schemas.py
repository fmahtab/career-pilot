from pydantic import BaseModel
from app.enums import ApplicationStatus
from typing import Optional


class JobApplication(BaseModel):
    company: str
    position: str
    status: ApplicationStatus
    application_url: Optional[str] = None
    job_description: Optional[str] = None

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class JobMatchRequest(BaseModel):
    job_description: str