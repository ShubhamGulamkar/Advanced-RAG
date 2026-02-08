# from fastapi import FastAPI, UploadFile, File
# from app.rag.loader import load_and_chunk
# from app.core.embeddings import get_embeddings
# from app.rag.pipeline import run_rag
# import pinecone
# from app.core.config import (
#     PINECONE_API_KEY,
#     PINECONE_ENV,
#     PINECONE_INDEX
# )

# app = FastAPI(title="Advanced RAG API")

# pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
# index = pinecone.Index(PINECONE_INDEX)
import tempfile
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pinecone import Pinecone,ServerlessSpec
from app.rag.loader import load_and_chunk
from app.core.embeddings import get_embeddings
from app.rag.pipeline import run_rag
from app.core.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)

app = FastAPI(title="Advanced RAG API")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)
# index = pc.create_index(
#     name="advanced-rag1",
#     dimension=1536,
#     metric="cosine",
#     spec=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     )
# )

# @app.post("/upload")
# async def upload(file: UploadFile = File(...)):
#     chunks = load_and_chunk(file)
#     embeddings = get_embeddings()

#     vectors = []
#     for i, chunk in enumerate(chunks):
#         vectors.append((
#             f"{file.filename}-{i}",
#             embeddings.embed_query(chunk.page_content),
#             {"text": chunk.page_content}
#         ))

#     index.upsert(vectors)
#     return {"message": f"{len(vectors)} chunks indexed"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        suffix = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        chunks = load_and_chunk(tmp_path)
        embeddings = get_embeddings()

        vectors = []
        for i, chunk in enumerate(chunks):
            vectors.append((
                f"{file.filename}-{i}",
                embeddings.embed_query(chunk.page_content),
                {"text": chunk.page_content}
            ))

        index.upsert(vectors)

        os.remove(tmp_path)

        return {
            "status": "success",
            "chunks_indexed": len(vectors)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
async def chat(query: str):
    answer = run_rag(query)
    return {"answer": answer}
