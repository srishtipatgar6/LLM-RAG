from src.text_splitter import split_text


def test_split_text():
    text = "A" * 1000

    chunks = split_text(
        text,
        chunk_size=200,
        chunk_overlap=20
    )

    assert len(chunks) > 1
    assert all(chunks)