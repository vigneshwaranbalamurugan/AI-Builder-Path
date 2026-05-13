from app.embeddings import create_embedding
from app.db import collection

def retrieve(query, k=4):

    embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    return results