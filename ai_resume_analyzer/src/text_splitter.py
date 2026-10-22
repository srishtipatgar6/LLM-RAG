from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_text(
    text,
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
):
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks