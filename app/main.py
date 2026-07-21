from fastapi import FastAPI, UploadFile, File
from pathlib import Path

from app.services.document_loader.pdf_loader import load_pdf

app = FastAPI(
    title="UX Research Copilot",
    description="AI assistant for UX research analysis",
    version="0.1.0"
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.get("/")
def home():
    return {
        "message": "UX Research Copilot is running 🚀"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    document = load_pdf(str(file_path))

    return document