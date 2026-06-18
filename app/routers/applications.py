from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import JobApplication
from app.models import Application
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()
applications = []

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
            "status": new_app.status
        }
    }


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
   
@router.get("/applications/{application_id}")
def get_applications(
    application_id: int,
    db: Session = Depends(get_db)
    ):
        application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
        )

        if not application:
            return {"error": "Application not found"}

        return{
            "id": application.id,
            "company": application.company,
            "position": application.position,
            "status": application.status
        }

@router.put("/applications/{application_id}")
def update_application(
    application_id: int,
    updated_application: JobApplication,
    db: Session = Depends(get_db)
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not application:
        return {"error": "Application not found"}
    
    application.company = updated_application.company,
    application.position = updated_application.position,
    application.status = updated_application.status

    db.commit()
    db.refresh(application)

    return {
         "message": "Application updated successfully",
         "application": {
              "id": application.id,
              "company": application.company,
              "position": application.position,
              "status": application.status
         }
    }

@router.delete("/applications/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = (
         db.query(Application)
         .filter(Application.id == application_id)
         .first()
    )

    if not application:
        return {"error": "Application not found"}
    
    deleted_id = application.id
    
    db.delete(application)
    db.commit()

    return {
         "message": "Application deleted successfully",
         "deleted_application_id": application_id
    }

