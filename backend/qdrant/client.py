from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333",
    timeout=60.0,   # ⬅ increase timeout (CRITICAL)
)
