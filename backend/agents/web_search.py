from langchain_core.tools import tool
from ddgs import DDGS

@tool
def web_search_tool(query: str) -> str:
    """Useful for finding information on the internet. Use this when you need current events, facts, or data not in your training memory."""
    try:
        print(f"--- Surfing the web for: '{query}' ---")
        
        # Use the DDGS API to search
        results = DDGS().text(query, max_results=5)
            
        if not results:
            return "No results found on the web."

        # Format the output so the AI can read it easily
        formatted_data = []
        for r in results:
            formatted_data.append(f"Title: {r['title']}\nSnippet: {r['body']}\nSource: {r['href']}")
            
        return "\n\n".join(formatted_data)
    
    except Exception as e:
        print(f"Search Error: {e}")
        return f"Sorry, I encountered an error while searching: {e}"