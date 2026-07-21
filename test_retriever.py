from app.services.embeddings.embedding_service import create_embedding
from app.services.vector_store.faiss_store import FAISSStore
from app.services.retrieval.retriever import Retriever


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


retriever = Retriever(
    store
)


results = retriever.retrieve(
    "Why do users leave checkout?"
)


for result in results:
    print(result)