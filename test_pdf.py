from app.services.document_loader.pdf_loader import load_pdf


result = load_pdf("data/uploads/Survey_opinions_text.pdf")

print(result["filename"])
print(result["pages"])
print(result["text"][:500])