from app.services.document_loader.pdf_loader import load_pdf
from app.services.text_processing.chunker import chunk_text


def process_document(file_path: str):
    document = load_pdf(file_path)

    chunks = chunk_text(
        document["pages"]
    )

    return {
        "filename": document["filename"],
        "chunks": chunks
    }