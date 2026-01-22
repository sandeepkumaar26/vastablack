import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from ddgs import DDGS

def scrape_website(url):
    """
    Visits a specific URL and extracts the main text content.
    """
    try:
        # Fake a browser user-agent so websites don't block us
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return ""

        soup = BeautifulSoup(response.content, "html.parser")
        
        # Remove navigation, scripts, and styles (noise)
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()

        # Get text and clean it up
        text = soup.get_text(separator=' ')
        lines = (line.strip() for line in text.splitlines())
        clean_text = ' '.join(chunk for chunk in lines if chunk)
        
        # Limit to first 4000 characters to prevent overwhelming the LLM
        return clean_text[:4000]

    except Exception as e:
        return ""

@tool
def deep_web_tool(query: str) -> str:
    """Use this for complex research questions. It searches the web AND reads the actual content of the websites to provide a comprehensive answer."""
    print(f"--- Deep Researching: '{query}' ---")
    
    compiled_data = []
    
    try:
        # Get top 3 search results
        results = DDGS().text(query, max_results=3)
        
        if not results:
            return "No results found."

        for idx, r in enumerate(results):
            url = r['href']
            title = r['title']
            print(f"   Reading Source {idx+1}: {url}...")
            
            # SCRAPE THE CONTENT
            content = scrape_website(url)
            
            if content:
                compiled_data.append(f"SOURCE {idx+1}: {title}\nURL: {url}\nCONTENT: {content}\n{'-'*40}")

        if not compiled_data:
            return "Found search results, but couldn't read the websites (they might block bots)."

        return "\n\n".join(compiled_data)

    except Exception as e:
        return f"Deep Research Error: {e}"