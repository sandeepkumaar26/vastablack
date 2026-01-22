#!/usr/bin/env python3
"""Test script for web_search.py"""

from backend.agents.web_search import web_search_tool

def main():
    print("=" * 60)
    print("Testing Web Search Tool")
    print("=" * 60)
    
    # Test the web search tool
    query = "Python programming latest news"
    print(f"\nSearching for: '{query}'\n")
    
    result = web_search_tool.invoke(query)
    
    print("\n" + "=" * 60)
    print("RESULTS:")
    print("=" * 60)
    print(result)
    print("\n" + "=" * 60)
    print("✓ Web search completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
