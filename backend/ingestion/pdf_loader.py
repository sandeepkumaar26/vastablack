from pypdf import PdfReader

def load_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.
    Returns a single string containing all text from the document.
    """
    try:
        reader = PdfReader(file_path)
        full_text = []

        print(f"   📄 Reading PDF: {len(reader.pages)} pages found.")
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text.append(text)
            else:
                print(f"   ⚠️ Warning: No text found on page {i+1} (might be an image).")
        
        # Join pages with spaces and clean up slightly
        return "\n".join(full_text)
    
    except Exception as e:
        print(f"❌ Error reading PDF {file_path}: {e}")
        return ""