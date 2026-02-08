import uvicorn
from app.api.app import app
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT
    )



# from pathlib import Path
# from llama_index.core import VectorStoreIndex
# from app.ingestion.loader import DocumentLoader
# from app.ingestion.chunker import AdvancedChunker
# from app.embeddings.embedder import get_embedding_model
# from app.vectorstore.faiss_store import create_faiss_store
# from app.core.logging import setup_logger

# logger = setup_logger("main")

# def main():
#     logger.info("Starting Advanced RAG System")

#     loader = DocumentLoader(Path("data/raw"))
#     docs = loader.load()

#     chunker = AdvancedChunker()
#     nodes = chunker.chunk(docs)

#     storage = create_faiss_store(dim=3072)

#     index = VectorStoreIndex(
#         nodes,
#         storage_context=storage,
#         embed_model=get_embedding_model()
#     )

#     logger.info("RAG system initialized successfully")

# if __name__ == "__main__":
#     main()
