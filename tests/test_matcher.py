from app.services.matcher import match_resume_to_job

resume_text = """
PHP
MySQL
FastAPI
Git
"""

job_description = """
Looking for a backend engineer with:

PHP
MySQL
Docker
AWS
"""

result = match_resume_to_job(
    resume_text,
    job_description
)

print(result)