from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings

# --- GLOBAL VARIABLES (initialized lazily) ---
_client = None
_vector_store = None
COLLECTION_NAME = "knowledge_base"

def get_client():
    """Lazy initialization of Qdrant client"""
    global _client
    if _client is None:
        _client = QdrantClient(path="./qdrant_data")
        
        # Safety check: create collection if missing
        if not _client.collection_exists(COLLECTION_NAME):
            print(f"--- ⚠️ Collection '{COLLECTION_NAME}' missing. Creating it now... ---")
            _client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE)
            )
    return _client

def get_vector_store():
    """Lazy initialization of vector store"""
    global _vector_store
    if _vector_store is None:
        client = get_client()
        embeddings = OllamaEmbeddings(
            model="nomic-embed-text",
            base_url="http://localhost:11434"
        )
        _vector_store = QdrantVectorStore(
            client=client,
            collection_name=COLLECTION_NAME,
            embedding=embeddings,
        )
    return _vector_store

# For backward compatibility - expose as module-level variable
# that gets initialized on first access
def __getattr__(name):
    if name == "client":
        return get_client()
    elif name == "vector_store":
        return get_vector_store()
    elif name == "retriever":
        return get_vector_store().as_retriever(search_kwargs={"k": 3})
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

def get_retriever(k: int = 3):
    store = get_vector_store()
    return store.as_retriever(search_kwargs={"k": k})