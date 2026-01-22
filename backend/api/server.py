from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Import the Agent Builder
from backend.agents.agent import build_agent

# Initialize the App
app = FastAPI(title="Convolve AI API")

# --- LOAD AGENT ONCE (At Startup) ---
# We do this here so we don't reload the model for every single request
print("Initializing AI Agent...")
try:
    agent_executor = build_agent()
    print("✓ AI Agent initialized successfully")
except Exception as e:
    print(f"✗ Failed to initialize AI Agent: {e}")
    raise

# --- DATA MODELS ---
# This defines what the JSON request body must look like
class QueryRequest(BaseModel):
    query: str

# --- ENDPOINTS ---

@app.get("/")
def health_check():
    return {"status": "active", "message": "Convolve AI System is Online"}

@app.post("/chat")
def chat_endpoint(request: QueryRequest):
    """
    Send a question to the AI Agent.
    Example Body: { "query": "What is the difficulty level?" }
    """
    user_query = request.query
    
    if not user_query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        # Run the Agent with langgraph's message-based input
        result = agent_executor.invoke({"messages": [HumanMessage(content=user_query)]})
        
        # Extract the final response from the messages
        final_message = result["messages"][-1]
        response_text = final_message.content
        
        return {
            "query": user_query,
            "response": response_text
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("backend.api.server:app", host="0.0.0.0", port=8000, reload=True)