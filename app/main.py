from fastapi import FastAPI, Depends

from app.database import Base, engine
from app import models
from app.routers.applications import router as application_router
from app.routers.auth import router as auth_router, get_current_user
from app.routers.resumes import router as resume_router


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(application_router)
app.include_router(auth_router)
app.include_router(resume_router)

# API welcome endpoint
@app.get("/")
def home():
    return {"message": "AI Job Tracker API"}

# Return the currently authenticated user
@app.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return{
        "id": current_user.id,
        "email": current_user.email
    }



   