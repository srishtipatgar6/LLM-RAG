import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def generate_response(prompt):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing in .env")

    client = Groq(
        api_key=GROQ_API_KEY
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content