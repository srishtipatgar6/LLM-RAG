
import streamlit as st

from src.pdf_loader import extract_text_from_pdf
from src.resume_analyzer import analyze_resume
from src.interview_questions import generate_interview_questions
from src.rag import add_resume_to_rag, ask_resume


st.set_page_config(
    page_title="Resume AI",
    page_icon="◈",
    layout="centered"
)

st.markdown("""
<style>
    * {
        box-sizing: border-box;
    }

    .stApp {
        background: #05070d;
        color: #f8fafc;
    }

    .main {
        background: #05070d;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    .top-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 18px;
        margin-bottom: 35px;
        background: #0b1020;
        border: 1px solid #1e293b;
        border-radius: 14px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
    }

    .brand-icon {
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: #2563eb;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 800;
    }

    .status {
        display: flex;
        align-items: center;
        gap: 7px;
        color: #94a3b8;
        font-size: 13px;
    }

    .status-dot {
        width: 7px;
        height: 7px;
        background: #3b82f6;
        border-radius: 50%;
        box-shadow: 0 0 10px #3b82f6;
    }

    .hero {
        text-align: center;
        margin-bottom: 42px;
    }

    .hero h1 {
        font-size: 42px;
        line-height: 1.1;
        font-weight: 750;
        color: #ffffff;
        margin: 0;
        letter-spacing: -1.5px;
    }

    .hero p {
        color: #94a3b8;
        font-size: 16px;
        margin-top: 12px;
    }

    .section-label {
        color: #cbd5e1;
        font-size: 14px;
        font-weight: 650;
        margin-bottom: 10px;
    }

    .input-card {
        background: #0b1020;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 16px;
    }

    .file-name {
        color: #60a5fa;
        font-size: 13px;
        margin-top: 8px;
    }

    .analysis-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-top: 42px;
        margin-bottom: 16px;
    }

    .analysis-icon {
        width: 34px;
        height: 34px;
        border-radius: 9px;
        background: #1d4ed8;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
    }

    .analysis-title {
        font-size: 19px;
        font-weight: 700;
        color: white;
    }

    .analysis-box {
        background: #0b1020;
        border: 1px solid #1e293b;
        border-left: 3px solid #2563eb;
        border-radius: 14px;
        padding: 24px 26px;
        color: #e2e8f0;
        line-height: 1.7;
    }

    .analysis-box h1,
    .analysis-box h2,
    .analysis-box h3 {
        color: #ffffff;
    }

    .analysis-box strong {
        color: #ffffff;
    }

    .analysis-box ul,
    .analysis-box ol {
        padding-left: 22px;
    }

    .analysis-box li {
        margin-bottom: 7px;
    }

    .chat-header {
        margin-top: 48px;
        margin-bottom: 18px;
        font-size: 19px;
        font-weight: 700;
        color: #ffffff;
    }

    .chat-subtitle {
        color: #64748b;
        font-size: 13px;
        margin-top: -12px;
        margin-bottom: 20px;
    }

    .user-message {
        background: #1d4ed8;
        color: white;
        padding: 12px 16px;
        border-radius: 16px 16px 4px 16px;
        margin: 18px 0 18px auto;
        max-width: 78%;
        width: fit-content;
        line-height: 1.5;
    }

    .assistant-message {
        background: #0b1020;
        border: 1px solid #1e293b;
        color: #e2e8f0;
        padding: 18px 20px;
        border-radius: 4px 16px 16px 16px;
        margin: 10px 0 24px 0;
        max-width: 90%;
        line-height: 1.7;
    }

    .assistant-message strong {
        color: #ffffff;
    }

    .interview-box {
        background: #0b1020;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 24px;
        margin-top: 15px;
        color: #e2e8f0;
        line-height: 1.7;
    }

    .divider {
        height: 1px;
        background: #172033;
        margin: 45px 0;
    }

    .footer {
        text-align: center;
        color: #475569;
        font-size: 12px;
        margin-top: 55px;
    }

    div.stButton > button {
        background: #2563eb;
        color: white;
        border: none;
        border-radius: 10px;
        height: 45px;
        font-weight: 650;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: #1d4ed8;
        border: none;
        color: white;
    }

    div.stButton > button:focus {
        box-shadow: 0 0 0 2px #60a5fa;
    }

    .stTextArea textarea {
        background: #080c16 !important;
        color: #f8fafc !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
    }

    .stTextArea textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 1px #2563eb !important;
    }

    .stTextInput input {
        background: #080c16 !important;
        color: #f8fafc !important;
        border: 1px solid #1e293b !important;
        border-radius: 12px !important;
    }

    .stTextInput input:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 1px #2563eb !important;
    }

    [data-testid="stFileUploader"] {
        background: #080c16;
        border: 1px dashed #334155;
        border-radius: 12px;
        padding: 8px;
    }

    [data-testid="stFileUploader"] section {
        background: transparent;
    }

    [data-testid="stFileUploader"] button {
        background: #172554;
        color: #bfdbfe;
        border: 1px solid #1d4ed8;
    }

    .stChatInput {
        border-color: #1e293b !important;
    }

    .stChatInput textarea {
        background: #0b1020 !important;
        color: white !important;
    }

    [data-testid="stChatInput"] {
        background: #0b1020 !important;
        border: 1px solid #334155 !important;
        border-radius: 16px !important;
    }

    [data-testid="stAlert"] {
        border-radius: 10px;
    }

    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }
</style>
""", unsafe_allow_html=True)


if "resume_text" not in st.session_state:
    st.session_state.resume_text = None

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = None

if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("""
<div class="top-bar">
    <div class="brand">
        <div class="brand-icon">R</div>
        Resume_Parser
    </div>
    <div class="status">
        <div class="status-dot"></div>
        LLM now connected
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>Your Resume. DECODED!</h1>
    <p>Analyze your resume-match it with a job-prepare for interviews.</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-label">Resume</div>',
    unsafe_allow_html=True
)

resume = st.file_uploader(
    "Upload resume",
    type=["pdf"],
    label_visibility="collapsed"
)

if resume:
    st.markdown(
        f'<div class="file-name">✓ {resume.name} ready</div>',
        unsafe_allow_html=True
    )


st.markdown(
    '<div class="section-label" style="margin-top:22px;">Job Description</div>',
    unsafe_allow_html=True
)

job_description = st.text_area(
    "Job Description",
    height=170,
    placeholder="Paste the job description here...",
    label_visibility="collapsed"
)


if st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True
):

    if resume is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter the job description.")

    else:

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_text_from_pdf(resume)

            if not resume_text:
                st.error("Could not extract text from this PDF.")
                st.stop()

            add_resume_to_rag(resume_text)

            result = analyze_resume(
                resume_text,
                job_description
            )

        st.session_state.resume_text = resume_text
        st.session_state.analysis = result
        st.session_state.messages = []
        st.session_state.interview_questions = None

        st.rerun()


if st.session_state.analysis:

    st.markdown("""
    <div class="analysis-header">
        <div class="analysis-icon">✦</div>
        <div class="analysis-title">Resume Analysis</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        st.session_state.analysis,
        unsafe_allow_html=False
    )


if st.session_state.resume_text:

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="chat-header">Chat with your resume</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="chat-subtitle">Ask questions about your experience, skills, projects, or education.</div>',
        unsafe_allow_html=True
    )


    for message in st.session_state.messages:

        if message["role"] == "user":

            st.markdown(
                f"""
                <div class="user-message">
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="assistant-message">',
                unsafe_allow_html=True
            )

            st.markdown(
                message["content"],
                unsafe_allow_html=False
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


    question = st.chat_input(
        "Ask anything about your resume..."
    )


    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.spinner("Thinking..."):

            answer = ask_resume(question)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()


    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="chat-header">Interview Preparation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="chat-subtitle">Generate questions tailored to your resume.</div>',
        unsafe_allow_html=True
    )


    if st.button(
        "Generate Interview Questions",
        use_container_width=True
    ):

        with st.spinner("Generating questions..."):

            questions = generate_interview_questions(
                st.session_state.resume_text
            )

        st.session_state.interview_questions = questions


    if st.session_state.interview_questions:

        st.markdown(
            '<div class="interview-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            st.session_state.interview_questions,
            unsafe_allow_html=False
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


st.markdown("""
<div class="footer">
    Resume AI · Powered by RAG & LLM
</div>
""", unsafe_allow_html=True)
