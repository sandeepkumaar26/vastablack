from langchain_core.tools import Tool
from ddgs import DDGS
from backend.qdrant.lc_bridge import retriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from backend.utils import process_and_index_url
import os

# --- Tool 1: Knowledge Base (Updated to modern LCEL approach) ---
# Get API key from environment variable
google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if google_api_key:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        temperature=0,
        google_api_key=google_api_key
    )
else:
    # Fallback to local Ollama if no Google API key is available
    from langchain_ollama import ChatOllama
    llm = ChatOllama(model="mistral-nemo", temperature=0)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question based on the provided context."),
    ("human", "Context: {context}\n\nQuestion: {question}")
])

# Format documents for context
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Create the RAG chain using LCEL
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def retrieve_knowledge(query):
    return rag_chain.invoke(query)

knowledge_tool = Tool(
    name="Knowledge_Base",
    func=retrieve_knowledge,
    description="Use this to answer questions based on PDFs you have ALREADY read."
)

# --- Tool 2: Web Search (UPGRADED) ---
def search_web_for_pdf(query):
    """
    Searches specifically for PDFs and returns a clean list of URLs.
    """
    try:
        print(f"--- 🔎 Searching Web for: {query} ---")
        # We specifically add 'filetype:pdf' to the query
        results = DDGS().text(f"{query} filetype:pdf", max_results=5)
        
        if not results:
            return "No PDF results found."
            
        # Format the output so the Agent sees clearly labeled URLs
        output = "Here are the PDF links found:\n"
        for res in results:
            output += f"- Title: {res['title']}\n  URL: {res['href']}\n"
        
        return output
            
    except Exception as e:
        return f"Search Error: {e}"

web_search_tool = Tool(
    name="Web_Search",
    func=search_web_for_pdf,
    description="Use this to find online PDF links. Input: a specific topic (e.g. 'Fusion Energy'). Returns a list of PDF URLs."
)

# --- Tool 3: PDF Reader (Keep as is) ---
read_pdf_tool = Tool(
    name="Read_PDF_URL",
    func=process_and_index_url,
    description="Use this to DOWNLOAD and READ a specific PDF URL found by search. Input: A valid http URL."
)