from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import JobApplication
from app.models import Application
from app.database import get_db

router = APIRouter()
applications = []

@router.post("/applications")
def create_application(application: JobApplication, db: Session = Depends(get_db)):
    new_app = Application(
        company=application.company,
        position=application.position,
        status=application.status
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
#def create_application(application: JobApplication):
#    applications.append(application.model_dump())

#    return{
#        "message": "Application Created",
#        "application": application.model_dump()
#    }


@router.get("/applications")
def get_applications(db: Session = Depends(get_db)):
    applications = db.query(Application).all()
   
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

