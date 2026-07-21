import fitz  # PyMuPDF
from pathlib import Path

def load_pdf(file_path: str):
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    return {
        "filename": Path(file_path).name,
        "pages": len(document),
        "text": text
    }