from typing import List

def chunk_text(
    text: str,
    chunk_size: int = 200,  # Reduced from 400 to fit MiniLM token limits
    overlap: int = 40
) -> List[str]:
    """
    Splits text into overlapping chunks of words.
    """
    if not text:
        return []

    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        
        # Join back into a string
        chunks.append(" ".join(chunk))
        
        # Move start pointer forward, but step back by overlap amount
        start = end - overlap

        # Prevent infinite loops if overlap >= chunk_size
        if start >= len(words): 
            break
            
    return chunks