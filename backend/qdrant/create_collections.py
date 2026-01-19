from qdrant_client.http import models
from .client import Qdrantclient

def create_collection(name, vector_size, distance, payload_schema):
    if client.collection_exists(name):
        print(f"[OK] Collection '{name}' already exists")
        return

    client.create_collection(
        collection_name=name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=distance
        )
    )

    print(f"[OK] Created collection '{name}'")

    # Create payload indexes safely
    for field, field_type in payload_schema.items():
        try:
            client.create_payload_index(
                collection_name=name,
                field_name=field,
                field_schema=field_type
            )
            print(f"[OK] Indexed field '{field}'")
        except Exception as e:
            print(f"[WARN] Skipped index for '{field}': {e}")
