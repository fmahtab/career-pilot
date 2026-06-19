from pydantic import BaseModel
from app.enums import ApplicationStatus


class JobApplication(BaseModel):
    company: str
    position: str
    status: ApplicationStatus

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class JobMatchRequest(BaseModel):
    job_description: str