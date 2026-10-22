from src.groq_client import generate_response
from src.prompts import INTERVIEW_QUESTIONS_PROMPT


def generate_interview_questions(resume_text):
    prompt = INTERVIEW_QUESTIONS_PROMPT.format(
        resume=resume_text
    )

    return generate_response(prompt)