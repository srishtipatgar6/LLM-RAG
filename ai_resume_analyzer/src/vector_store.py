import chromadb
from src.config import CHROMA_DB_PATH


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    return client.get_or_create_collection(name="resume")


def add_documents(chunks, embeddings):
    collection = get_collection()

    ids = [f"resume_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )


def search(embedding, top_k=3):
    collection = get_collection()

    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )