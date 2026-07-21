from app.services.pipeline.document_pipeline import process_document


result = process_document(
    "data/uploads/Survey_opinions_text.pdf"
)


print(result["filename"])

print(
    "Number of chunks:",
    len(result["chunks"])
)


for chunk in result["chunks"]:
    print("\n---")
    print("Chunk:", chunk["chunk_id"])
    print("Page:", chunk["page"])
    print(chunk["text"][:200])