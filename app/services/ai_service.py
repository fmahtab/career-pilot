def generate_cover_letter(
    resume_text: str,
    job_description: str,
) -> str:
    """
    Generate a tailored cover letter using AI.

    This implementation currently returns a mock response.
    It will later be replaced with a Claude API call.
    """

    resume_summary = resume_text[:1000]
    job_summary = job_description[:1000]

    return f"""
Dear Hiring Manager,

I am excited to apply for this opportunity.

Based on my experience and the job requirements, I believe I would be a strong addition to your team.

Resume Summary:
{resume_summary}

Job Description Summary:
{job_summary}

Thank you for your consideration.

Sincerely,
Candidate
"""