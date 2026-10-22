from src.groq_client import generate_response
from src.prompts import RESUME_ANALYSIS_PROMPT


def analyze_resume(
    resume_text,
    job_description
):
    prompt = RESUME_ANALYSIS_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    return generate_response(prompt)