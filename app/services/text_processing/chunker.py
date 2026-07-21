def chunk_text(pages, chunk_size=1000, overlap=200):
    chunks = []

    chunk_id = 1

    for page in pages:
        text = page["text"]
        page_number = page["page_number"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "text": chunk,
                    "page": page_number
                }
            )

            chunk_id += 1

            start += chunk_size - overlap

    return chunks