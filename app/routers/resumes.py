import os
from fastapi import APIRouter, Depends, UploadFile, File

from app.routers.auth import get_current_user

from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Resume

router = APIRouter()

UPLOAD_DIR = "uploads/resumes"

@router.post("/resumes/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    file_path = os.path.join(
        UPLOAD_DIR,
        f"user_{current_user.id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    new_resume = Resume(
        filename = file.filename,
        file_path = file_path,
        user_id = current_user.id
    )

    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "saved_path": file_path,
        "user_id": current_user.id
    }

@router.get("/resumes")
def get_resumes(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    resumes = (
        db.query(Resume)
        .filter(Resume.user_id == current_user.id)
        .all()
    )
    return {
        "count": len(resumes),
        "resumes": [
            {
                "id": resume.id,
                "filename": resume.filename,
                "file_path": resume.file_path
            }
            for resume in resumes
        ]
    }