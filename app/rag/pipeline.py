from app.rag.retriever import retrieve
from app.rag.reranker import rerank
from app.core.llm import get_llm

def run_rag(query):
    retrieved_docs = retrieve(query)
    contexts = retrieved_docs
    reranked_docs = rerank(query, retrieved_docs)

    context = "\n\n".join(reranked_docs)

    prompt = f"""
        You are a strict document-based assistant.
        Answer ONLY using the provided context.
        If the answer is not present, say:
        "I don’t know based on the given documents.
Context:
{context}

Question:
{query}
"""

    llm = get_llm()
    response = llm.invoke(prompt)
    return {
        "answer":response.content,
        "contexts": contexts}

