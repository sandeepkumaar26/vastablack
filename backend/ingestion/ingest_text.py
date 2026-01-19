import uuid
from ingestion.text_loader import load_text
from ingestion.text_chunker import chunk_text
from ingestion.metadata_builder import build_metadata
from embeddings.text_embeddings import embed_text
from qdrant.client import qdrant_client

COLLECTION_NAME = "text_documents"

def ingest_text_document(
    file_path: str,
    doc_id: str,
    title: str,
    domain: str,
    difficulty_level: str,
    source: str
):
    text = load_text(file_path)
    chunks = chunk_text(text)

    points = []

    for idx, chunk in enumerate(chunks):
        vector = embed_text(chunk)
        payload = build_metadata(
            doc_id=doc_id,
            title=title,
            domain=domain,
            difficulty_level=difficulty_level,
            source=source,
            chunk_index=idx
        )

        payload["text"] = chunk

        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": payload
        })

    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"✅ Ingested {len(points)} chunks into {COLLECTION_NAME}")
