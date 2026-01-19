def chunk_text(
    text: str,
    chunk_size: int = 400,
    overlap: int = 80
):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start = end - overlap

    return chunks
