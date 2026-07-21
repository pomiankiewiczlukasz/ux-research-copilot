from pathlib import Path
import fitz  # PyMuPDF


def load_pdf(file_path: str):
    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        pages.append(
            {
                "page_number": page_number,
                "text": page.get_text()
            }
        )

    return {
        "filename": Path(file_path).name,
        "pages": pages
    }