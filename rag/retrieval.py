import numpy as np
from config import TOP_K
from rag.embeddings import create_embedding
from database.sqlite_manager import get_all_chunks


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return float(np.dot(a, b) / denominator)


def retrieve(query, top_k=TOP_K):
    query_embedding = create_embedding(query)

    rows = get_all_chunks()

    scores = []

    for source, content, embedding in rows:
        embedding = np.array(eval(embedding))

        score = cosine_similarity(
            query_embedding,
            embedding
        )

        scores.append((score, source, content))

    scores.sort(reverse=True, key=lambda x: x[0])

    return scores[:top_k]
