RESUME_ANALYSIS_PROMPT = """
You are an AI Resume Analyzer.

Analyze the resume against the job description.

Resume:
{resume}

Job Description:
{job_description}

Return:

Overall Match: X/100

Experience Match: X/10

Skills Match: X/10

Matched Skills:
- skill

Missing Skills:
- skill

Suggestions:
- suggestion

Base the analysis only on the provided resume and job description.
Do not invent skills, experience, or qualifications.
"""


ASK_RESUME_PROMPT = """
Answer the user's question using only the resume context.

Resume Context:
{context}

Question:
{question}

If the answer is not available in the resume context,
say that the information is not available in the resume.
"""


INTERVIEW_QUESTIONS_PROMPT = """
Generate interview questions based on the candidate's resume.

Resume:
{resume}

Generate:

Technical Questions:
1.
2.
3.
4.
5.

Project Questions:
1.
2.
3.

Behavioral Questions:
1.
2.
"""