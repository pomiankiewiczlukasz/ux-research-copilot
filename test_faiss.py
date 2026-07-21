from app.services.embeddings.embedding_service import create_embedding
from app.services.vector_store.faiss_store import FAISSStore


documents = [
    "Users abandon carts because checkout is too long.",
    "Users struggle with product filters.",
    "Customers like fast delivery options."
]


embeddings = [
    create_embedding(doc)
    for doc in documents
]


store = FAISSStore(
    dimension=384
)


store.add(
    embeddings,
    documents
)


question = "Why do customers leave the shopping process?"


query_embedding = create_embedding(
    question
)


results = store.search(
    query_embedding,
    k=2
)


print("Search results:")

for result in results:
    print("- ", result)