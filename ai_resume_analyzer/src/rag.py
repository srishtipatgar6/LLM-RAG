from src.text_splitter import split_text
from src.embeddings import generate_embeddings
from src.vector_store import add_documents, search
from src.groq_client import generate_response
from src.prompts import ASK_RESUME_PROMPT


def add_resume_to_rag(resume_text):
    chunks = split_text(resume_text)

    if not chunks:
        return

    embeddings = generate_embeddings(chunks)

    add_documents(
        chunks,
        embeddings
    )


def retrieve_context(query, top_k=3):
    query_embedding = generate_embeddings([query])[0]

    results = search(
        query_embedding,
        top_k
    )

    documents = results.get("documents", [[]])

    if not documents or not documents[0]:
        return ""

    return "\n\n".join(documents[0])


def ask_resume(question):
    context = retrieve_context(question)

    prompt = ASK_RESUME_PROMPT.format(
        context=context,
        question=question
    )

    return generate_response(prompt)