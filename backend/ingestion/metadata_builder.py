from datetime import datetime, timezone

def build_metadata(
    doc_id: str,
    title: str,
    domain: str,
    difficulty_level: str,
    source: str,
    chunk_index: int
) -> dict:
    """
    Constructs a standardized metadata dictionary for vector payloads.
    """
    return {
        "doc_id": doc_id,
        "title": title,
        "domain": domain,
        "difficulty_level": difficulty_level,
        "content_type": "research_paper",  # You might want to make this dynamic later
        "language": "en",
        "source": source,
        "chunk_index": chunk_index,
        # Use timezone-aware UTC time
        "created_at": datetime.now(timezone.utc).isoformat(),
        "usage_count": 0
    }