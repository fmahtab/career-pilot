import os
from fastapi import APIRouter, Depends, UploadFile, File
from app.routers.auth import get_current_user
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Resume
from app.services.resume_parser import extract_text_from_resume
from app.schemas import JobMatchRequest
from app.services.matcher import match_resume_to_job
from pathlib import Path
import re

router = APIRouter()

UPLOAD_DIR = "uploads/resumes"
ALLOWED_EXTENSIONS = [".pdf", ".docx"]
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Upload and parse a resume file
@router.post("/resumes/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    extension = Path(file.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        return {"error": "Only PDF and DOCX files are allowed"}

    safe_filename = re.sub(r"[^a-zA-Z0-9_.-]", "_", file.filename)

    file_path = f"{UPLOAD_DIR}/user_{current_user.id}_{safe_filename}"

    file_content = file.file.read()

    if len(file_content) > MAX_FILE_SIZE:
        return {"error": "File size must be 5 MB or less"}

    with open(file_path, "wb") as buffer:
        buffer.write(file_content)

    resume_text = extract_text_from_resume(file_path)

    print(f"Parsed {len(resume_text)} characters from resume")

    new_resume = Resume(
        filename=safe_filename,
        file_path=file_path,
        user_id=current_user.id,
        parsed_text=resume_text
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

# Return all resumes belonging to the current user
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

# Return a specific resume owned by the current user
@router.get("/resumes/{resume_id}")
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    resume = (
        db.query(Resume)
        .filter(
            Resume.id == resume_id,
            Resume.user_id == current_user.id
        )
        .first()
    )

    if not resume:
        return {
            "error": "Resume not found"
        }
    
    return {
        "id": resume.id,
        "filename": resume.filename,
        "file_path": resume.file_path 
    }

# Delete a specific resume owned by the current user
@router.delete("/resumes/{resume_id}")
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    resume = (
        db.query(Resume)
        .filter(
            Resume.id == resume_id,
            Resume.user_id == current_user.id
        )
        .first()
    )

    if not resume:
        return {
            "error": "Resume not found"
        }

    deleted_id = resume.id

    db.delete(resume)
    db.commit()

    return {
        "message": "Resume deleted successfully",
        "deleted_resume_id": deleted_id
    }

# Match a resume against a job description
@router.post("/resumes/{resume_id}/match")
def match_resume(
    resume_id: int,
    request: JobMatchRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    resume = (
        db.query(Resume)
        .filter(
            Resume.id == resume_id,
            Resume.user_id == current_user.id
        )
        .first()
    )
    
    if not resume:
        return{
            "error": "Resume not found"
        }
    
    if not resume.parsed_text:
        return {
            "error": "This resume has no parsed text. Please upload it again."
        }

    result = match_resume_to_job(
        resume.parsed_text,
        request.job_description
    )

    return result