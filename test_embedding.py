from app.services.embeddings.embedding_service import create_embedding


text = """
Users abandon checkout because shipping costs appear too late.
"""


embedding = create_embedding(text)


print("Embedding size:", len(embedding))
print("First values:")
print(embedding[:10])