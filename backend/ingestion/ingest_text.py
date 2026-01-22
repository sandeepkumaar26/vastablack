import uuid
from backend.ingestion.text_loader import load_text
from backend.ingestion.text_chunker import chunk_text
from backend.ingestion.metadata_builder import build_metadata
from backend.embeddings.text_embeddings import generate_embeddings  # Renamed from embed_text
from backend.qdrant.client import client  # Renamed from qdrant_client
from qdrant_client.models import PointStruct
from backend.ingestion.pdf_loader import load_pdf

COLLECTION_NAME = "text_documents"

def ingest_text_document(
    file_path: str,
    doc_id: str,
    title: str,
    domain: str,
    difficulty_level: str,
    source: str
):
    print(f"📖 Loading file: {file_path}")
    if file_path.endswith(".pdf"):
        text = load_pdf(file_path)
    else:
        text = load_text(file_path)
    
    print(f"✂️ Chunking text...")
    chunks = chunk_text(text)
    if not chunks:
        print("⚠️ Warning: No chunks generated. Skipping ingestion.")
        return

    print(f"🧠 Generating embeddings for {len(chunks)} chunks...")
    vectors = generate_embeddings(chunks)

    points = []
    for idx, (chunk, vector) in enumerate(zip(chunks, vectors)):
        payload = build_metadata(
            doc_id=doc_id,
            title=title,
            domain=domain,
            difficulty_level=difficulty_level,
            source=source,
            chunk_index=idx
        )
        
        # Ensure the actual text is in the payload for retrieval
        payload["text"] = chunk
        
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload=payload
        ))

    # 4. Upsert to Qdrant
    print(f"🚀 Upserting {len(points)} points to Qdrant...")
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
        wait=True 
    )

    print(f"✅ Ingested {len(points)} chunks into '{COLLECTION_NAME}'")