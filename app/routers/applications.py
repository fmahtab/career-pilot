from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import JobApplication
from app.models import Application, Resume
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()

# Create a new job application
@router.post("/applications")
def create_application(
    application: JobApplication, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_app = Application(
        company=application.company,
        position=application.position,
        status=application.status,
        application_url=application.application_url,
        job_description = application.job_description,
        user_id=current_user.id
    )

    db.add(new_app)
    db.commit()
    db.refresh(new_app)

    return {
        "message": "Application created",
        "application": {
            "id": new_app.id,
            "company": new_app.company,
            "position": new_app.position,
            "status": new_app.status,
            "application_url": new_app.application_url,
            "job_description": new_app.job_description
        }
    }


# Return all applications belonging to the current user
@router.get("/applications")
def get_applications(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)    
):
    applications = (
        db.query(Application)
        .filter(Application.user_id == current_user.id)
        .all()
    )
   
    return{
        "count": len(applications),
        "applications": [
            {
            "id": app.id,
            "company": app.company,
            "position": app.position,
            "status": app.status
            }
            for app in applications
        ]
    }
   
# Return a specific application owned by the current user
@router.get("/get_application/{application_id}")
def get_applications(
    application_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    application = (
    db.query(Application)
    .filter(
        Application.id == application_id,
        Application.user_id == current_user.id
    )
    .first()
    )

    if not application:
        return {"error": "Application not found"}

    return{
        "id": application.id,
        "company": application.company,
        "position": application.position,
        "status": application.status,
        "application_url": application.application_url,
        "job_description": application.job_description,
        "cover_letter": application.cover_letter
    }

# Update a specific application owned by the current user
@router.put("/applications/{application_id}")
def update_application(
    application_id: int,
    updated_application: JobApplication,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    application = (
        db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
        .first()
    )

    if not application:
        return {"error": "Application not found"}
    
    application.company = updated_application.company
    application.position = updated_application.position
    application.status = updated_application.status
    application.application_url = updated_application.application_url
    application.job_description = updated_application.job_description

    db.commit()
    db.refresh(application)

    return {
         "message": "Application updated successfully",
         "application": {
            "id": application.id,
            "company": application.company,
            "position": application.position,
            "status": application.status,
            "application_url": application.application_url,
            "job_description": application.job_description
         }
    }

# Delete a specific application owned by the current user
@router.delete("/applications/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    application = (
         db.query(Application)
         .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
         .first()
    )

    if not application:
        return {"error": "Application not found"}
    
    deleted_id = application.id
    
    db.delete(application)
    db.commit()

    return {
         "message": "Application deleted successfully",
         "deleted_application_id": deleted_id
    }

# Generate an AI-powered cover letter for a job application
@router.post("/applications/{application_id}/cover-letter")
def generate_cover_letter(
    application_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    application = (db.query(Application)
        .filter(
            Application.id == application_id,
            Application.user_id == current_user.id
        )
        .first()
    )

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    resume = (db.query(Resume)
        .filter(
            Resume.user_id == current_user.id
        )
        .order_by(
            Resume.id.desc()
        )
        .first()
    )


    if not resume or not resume.parsed_text:
            raise HTTPException(status_code=400, detail="Parsed resume text is required")


    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the {application.position} role at {application.company}.

Based on my background and the job description, I believe my experience aligns well with this opportunity.

[AI-generated content goes here.]

Sincerely,
{current_user.email}
"""
    
    application.cover_letter = cover_letter
    db.commit()
    db.refresh(application)

    return {
        "application_id": application.id,
        "cover_letter": cover_letter
    }
