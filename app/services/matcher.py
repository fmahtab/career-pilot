COMMON_SKILLS = [
    "PHP",
    "Python",
    "JavaScript",
    "TypeScript",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "REST",
    "REST API",
    "FastAPI",
    "Laravel",
    "WordPress",
    "Git",
    "Redis",
    "RabbitMQ"
]

def extract_skills(text: str):
    found_skills = []

    text_lower = text.lower()

    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills

def match_resume_to_job(resume_text: str, job_description: str):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matching_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matching_skills.append(skill)

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)
    
    if len(job_skills) == 0:
        matching_score = 0
    else:
        matching_score = int((len(matching_skills) / len(job_skills)) * 100)
    
    return {
        "match_score": matching_score,
        "matching_skills": matching_skills,
        "missing_skills": missing_skills
    }

