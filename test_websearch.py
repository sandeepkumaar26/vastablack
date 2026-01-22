"""Test script to verify DuckDuckGo web search integration"""
from backend.agents.web_search import web_search_tool

def test_web_search():
    print("Testing DuckDuckGo web search tool...")
    print("-" * 50)
    
    try:
        # Test the web search tool
        query = "What is Python programming language?"
        print(f"Query: {query}\n")
        
        result = web_search_tool.invoke(query)
        
        print("Search Results:")
        print(result)
        print("-" * 50)
        print("SUCCESS: Web search working!")
        return True
        
    except Exception as e:
        print(f"FAILED: Web search error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_web_search()