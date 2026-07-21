from app.services.embeddings.embedding_service import create_embedding


class Retriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store


    def retrieve(self, question: str, k=3):

        question_embedding = create_embedding(
            question
        )

        results = self.vector_store.search(
            question_embedding,
            k
        )

        return results