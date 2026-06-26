import os
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()

client = Anthropic(
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

ANTHROPIC_MODEL = os.getenv(
    "ANTHROPIC_MODEL",
    "claude-3-5-haiku-latest"
)

def generate_cover_letter(
    resume_text: str,
    job_description: str,
) -> str:
    """
    Generate a tailored cover letter using Claude.
    """

    prompt = f"""
You are an experienced technical recruiter and hiring manager for software engineering roles.

Write a personalized cover letter based on the candidate's resume and the job description.

Requirements:

- Keep the cover letter between 200 and 300 words.
- Start with "Dear Hiring Manager,".
- Do NOT include the candidate's name, phone number, email, address, LinkedIn profile, resume header, or any contact information.
- Do NOT copy or summarize the resume verbatim.
- Do NOT invent or exaggerate skills or experience.
- Highlight only experience that is supported by the resume.
- Focus on the 3–4 qualifications that are most relevant to the job description.
- Use 4 short paragraphs maximum.
- Avoid phrases like "I am writing to express my interest".
- Make it sound natural and direct.
- Explain why the candidate is a strong fit for this specific role.
- Use a natural, confident, and professional tone.
- Keep paragraphs concise (2–4 sentences).
- Avoid repeating similar technical achievements.
- Do NOT mention skills or technologies that are not relevant to the job description.
- End with:

Thank you for your consideration.

Sincerely,

Return only the cover letter. Do not include explanations, markdown, or any additional text.

Candidate Resume:
{resume_text[:4000]}

Job Description:
{job_description[:3000]}
"""

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=400,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return response.content[0].text