

from langchain_openai import OpenAIEmbeddings
from app.core.config import OPENAI_API_KEY

def get_embeddings():
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENAI_API_KEY
    )
# from langchain_openai import OpenAIEmbeddings

# def get_embeddings():
#     return OpenAIEmbeddings(model="text-embedding-3-large")
