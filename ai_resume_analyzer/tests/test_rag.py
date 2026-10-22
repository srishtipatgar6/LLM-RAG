from src.rag import retrieve_context


def test_rag_import():
    assert callable(retrieve_context)