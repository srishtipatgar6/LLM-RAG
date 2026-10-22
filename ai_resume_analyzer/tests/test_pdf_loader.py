from src.pdf_loader import extract_text_from_pdf


def test_pdf_loader_import():
    assert callable(extract_text_from_pdf)