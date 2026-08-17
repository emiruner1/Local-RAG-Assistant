import numpy as np

from database.sqlite_manager import get_all_chunks
from rag.embeddings import create_embedding, json_to_embedding


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve(query, top_k=3):
    query_embedding = create_embedding(query)

    rows = get_all_chunks()

    scores = []

    for source, content, embedding in rows:
        score = cosine_similarity(
            query_embedding,
            json_to_embedding(embedding)
        )

        scores.append((score, source, content))

    scores.sort(reverse=True)

    return scores[:top_k]