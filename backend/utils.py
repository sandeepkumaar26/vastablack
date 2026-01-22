import os
import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.qdrant.lc_bridge import get_vector_store

def process_and_index_url(url: str):
    """
    Downloads a PDF from a URL, splits it, and adds it to Qdrant.
    """
    filename = url.split("/")[-1] or "downloaded_doc.pdf"
    # Clean filename to avoid errors
    filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in "._-"])
    temp_file = f"temp_{filename}"
    
    try:
        print(f"--- 📥 Agent Downloading PDF: {url} ---")
        # Fake user agent to avoid being blocked by sites
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return f"Failed to download. Status code: {response.status_code}"
            
        with open(temp_file, "wb") as f:
            f.write(response.content)
            
        # Load & Split
        loader = PyPDFLoader(temp_file)
        docs = loader.load()
        
        if not docs:
            return "Downloaded file, but it seems empty or not a valid PDF."

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        
        # Add metadata
        for doc in splits:
            doc.metadata["source"] = url

        # Index to Qdrant - use lazy initialization
        vector_store = get_vector_store()
        vector_store.add_documents(splits)
        return f"Successfully read and indexed {len(splits)} chunks from the PDF."
        
    except Exception as e:
        return f"Error processing PDF: {str(e)}"
        
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)