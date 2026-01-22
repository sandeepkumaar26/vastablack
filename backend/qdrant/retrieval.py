from backend.qdrant.lc_bridge import get_retriever

def get_context(query: str, k: int = 3) -> str:
    """
    Retrieves relevant documents and formats them into a single context string
    suitable for passing to an LLM.
    """
    retriever = get_retriever(k=k)
    
    # LangChain's invoke() handles the embedding and search automatically
    docs = retriever.invoke(query)
    
    if not docs:
        return ""

    # Format the output nicely for the LLM
    context_parts = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        content = doc.page_content
        context_parts.append(f"[Document {i} | Source: {source}]\n{content}")
    
    return "\n\n".join(context_parts)