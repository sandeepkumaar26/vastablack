from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langgraph.prebuilt import create_react_agent
import os

# --- IMPORT TOOLS ---
from backend.agents.tools import knowledge_tool
from backend.agents.deep_web import deep_web_tool
from backend.agents.web_search import web_search_tool

def build_agent(model_name="mistral-nemo"):
    # 1. Define Tools
    # We give the agent:
    # - Knowledge Base (for your PDFs)
    # - Deep Web (for online research)
    # - Web Search (for quick searches)
    tools = [knowledge_tool, deep_web_tool, web_search_tool]

    # 2. Define the Brain (LLM)
    # Use Google Gemini if API key is available, otherwise use Ollama
    google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    
    if google_api_key:
        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=google_api_key)
        print(f"✓ Using Google Gemini AI")
    else:
        # Use Ollama local model
        llm = ChatOllama(model=model_name, temperature=0)
        print(f"✓ Using Ollama model: {model_name}")

    # 3. Define the Prompt
    template = '''You are an Advanced Research Assistant.
    
    TOOLS:
    ------
    You have access to these tools:
    
    {tools}
    
    STRATEGY:
    1. Always check the 'Knowledge_Base' (uploaded PDFs) first.
    2. If the answer is not in the PDFs, use 'deep_web_tool' to search online and read full content.
    3. For quick searches, use 'web_search_tool'.
    4. Provide citations or URLs if you found them online.

    Question: {input}
    '''

    # 4. Create Agent using LangGraph
    agent = create_react_agent(llm, tools)
    
    return agent