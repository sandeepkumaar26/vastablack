# Vastablack AI Research Assistant

An advanced AI-powered research assistant that combines Retrieval-Augmented Generation (RAG), web search, and deep web scraping capabilities to provide comprehensive, well-researched answers to complex queries.

## 🌟 Features

- **RAG-based Knowledge Base**: Upload and query PDF documents using vector embeddings and semantic search
- **Web Search Integration**: Quick web searches using DuckDuckGo for current information
- **Deep Web Research**: Automated web scraping and content extraction from multiple sources
- **Multi-Model Support**: 
  - Google Gemini (cloud-based, recommended)
  - Ollama (local AI models like Mistral-Nemo)
- **Modern Tech Stack**: Built with LangGraph, LangChain, FastAPI, and Streamlit
- **Vector Database**: Powered by Qdrant for efficient semantic search
- **Interactive UI**: Clean Streamlit interface for easy interaction

## 🏗️ Architecture

```
┌─────────────────┐
│  Streamlit UI   │
│  (Frontend)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   FastAPI       │
│  (Backend API)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│      LangGraph Agent            │
│  ┌──────────────────────────┐   │
│  │  Tools:                  │   │
│  │  • Knowledge Base (RAG)  │   │
│  │  • Web Search            │   │
│  │  • Deep Web Scraper      │   │
│  └──────────────────────────┘   │
└─────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│  Qdrant Vector  │
│    Database     │
└─────────────────┘
```

## 📋 Prerequisites

- Python 3.10 or higher
- One of the following:
  - Google Gemini API key (recommended, free tier available)
  - Ollama with installed models (for local AI)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sandeepkumaar26/vastablack.git
   cd vastablack
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

## ⚙️ Configuration

### Option 1: Using Google Gemini (Recommended)

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

### Option 2: Using Ollama (Local AI)

1. Install Ollama from [ollama.com](https://ollama.com/download)
2. Pull a model:
   ```bash
   ollama pull mistral-nemo
   ```
3. No API key needed - the system will automatically use Ollama

## 🎯 Usage

### Starting the Backend Server

```bash
python -m uvicorn backend.api.server:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:
- API: http://127.0.0.1:8000
- API Docs: http://127.0.0.1:8000/docs

### Starting the Frontend

```bash
streamlit run frontend/app.py
```

The Streamlit UI will be available at http://localhost:8501

### Using the Application

1. Open http://localhost:8501 in your browser
2. Type your question in the chat interface
3. The AI agent will:
   - Check the knowledge base for relevant information
   - Search the web if needed
   - Scrape and read website content for comprehensive answers
   - Provide sourced, well-researched responses

## 📁 Project Structure

```
vastablack/
├── backend/
│   ├── agents/
│   │   ├── agent.py          # Main LangGraph agent
│   │   ├── tools.py          # RAG knowledge base tool
│   │   ├── web_search.py     # Web search tool
│   │   └── deep_web.py       # Deep web scraping tool
│   ├── api/
│   │   └── server.py         # FastAPI server
│   ├── embeddings/
│   │   └── text_embeddings.py # Embedding models
│   ├── ingestion/
│   │   ├── pdf_loader.py     # PDF document processing
│   │   └── text_chunker.py   # Text chunking
│   ├── qdrant/
│   │   ├── client.py         # Qdrant client
│   │   └── lc_bridge.py      # LangChain-Qdrant bridge
│   ├── utils.py              # Utility functions
│   └── requirements.txt      # Python dependencies
├── frontend/
│   └── app.py                # Streamlit UI
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🛠️ Technologies Used

- **AI/ML Frameworks**:
  - LangGraph - Agent orchestration
  - LangChain - LLM integration
  - Sentence Transformers - Text embeddings
  
- **LLM Providers**:
  - Google Gemini (via langchain-google-genai)
  - Ollama (via langchain-ollama)
  
- **Vector Database**:
  - Qdrant - Vector storage and similarity search
  
- **Backend**:
  - FastAPI - REST API framework
  - Uvicorn - ASGI server
  
- **Frontend**:
  - Streamlit - Interactive web UI
  
- **Web Tools**:
  - DDGS - DuckDuckGo search
  - BeautifulSoup4 - Web scraping
  - Requests - HTTP client

## 🔧 API Endpoints

### POST /chat
Send a query to the AI agent

**Request:**
```json
{
  "query": "What is quantum computing?"
}
```

**Response:**
```json
{
  "query": "What is quantum computing?",
  "response": "Quantum computing is..."
}
```

### GET /
Health check endpoint

**Response:**
```json
{
  "status": "active",
  "message": "Convolve AI System is Online"
}
```

## 📝 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | No* |
| `GEMINI_API_KEY` | Alternative for Google API key | No* |

*One of the API keys is required unless using Ollama

## 🐛 Troubleshooting

### Error 500: Model not found

**Problem**: The system can't find the AI model.

**Solutions**:
1. If using Google Gemini: Set your `GOOGLE_API_KEY` in `.env`
2. If using Ollama: 
   - Check Ollama is running: `ollama list`
   - Pull the model: `ollama pull mistral-nemo`

### Qdrant lock error

**Problem**: `Storage folder ./qdrant_data is already accessed by another instance`

**Solution**: Stop all Python processes and restart the backend server

### Connection refused on port 8000

**Problem**: Backend server is not running.

**Solution**: Start the backend with:
```bash
python -m uvicorn backend.api.server:app --reload --host 127.0.0.1 --port 8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Sandeep Kumar**
- GitHub: [@sandeepkumaar26](https://github.com/sandeepkumaar26)

## 🙏 Acknowledgments

- Google for Gemini AI
- Ollama for local LLM support
- LangChain and LangGraph teams
- Qdrant for vector database
- Streamlit for the amazing UI framework

---

Made with ❤️ using LangGraph and modern AI technologies
