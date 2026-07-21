import faiss
import numpy as np


class FAISSStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []


    def add(self, embeddings, documents):
        vectors = np.array(
            embeddings
        ).astype("float32")

        self.index.add(vectors)

        self.documents.extend(documents)


    def search(self, query_embedding, k=3):
        vector = np.array(
            [query_embedding]
        ).astype("float32")

        distances, indices = self.index.search(
            vector,
            k
        )

        results = []

        for idx in indices[0]:
            results.append(
                self.documents[idx]
            )

        return results