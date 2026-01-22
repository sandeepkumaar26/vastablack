from sentence_transformers import SentenceTransformer
from typing import List

print("⏳ Loading embedding model...")
MODEL_NAME = 'all-MiniLM-L6-v2'
model = SentenceTransformer(MODEL_NAME)
print("✅ Embedding model loaded.")

def generate_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Generates vector embeddings for a list of text strings.
    """
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings.tolist()