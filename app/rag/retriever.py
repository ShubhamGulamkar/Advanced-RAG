from pinecone import Pinecone
from app.core.config import PINECONE_API_KEY, PINECONE_INDEX
from app.core.embeddings import get_embeddings

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def retrieve(query, top_k=8):
    embeddings = get_embeddings()
    query_vector = embeddings.embed_query(query)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return [m["metadata"]["text"] for m in results["matches"]]


# import pinecone
# from app.core.config import (
#     PINECONE_API_KEY,
#     PINECONE_ENV,
#     PINECONE_INDEX
# )
# from app.core.embeddings import get_embeddings

# pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
# index = pinecone.Index(PINECONE_INDEX)

# def retrieve(query, top_k=8):
#     embeddings = get_embeddings()
#     query_vector = embeddings.embed_query(query)

#     results = index.query(
#         vector=query_vector,
#         top_k=top_k,
#         include_metadata=True
#     )

#     return [m["metadata"]["text"] for m in results["matches"]]

