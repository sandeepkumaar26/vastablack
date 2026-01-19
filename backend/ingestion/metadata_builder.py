from datetime import datetime

def build_metadata(
    doc_id: str,
    title: str,
    domain: str,
    difficulty_level: str,
    source: str,
    chunk_index: int
):
    return {
        "doc_id": doc_id,
        "title": title,
        "domain": domain,
        "difficulty_level": difficulty_level,
        "content_type": "research_paper",
        "language": "en",
        "source": source,
        "chunk_index": chunk_index,
        "created_at": datetime.utcnow().isoformat(),
        "usage_count": 0
    }
