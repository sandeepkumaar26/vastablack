import streamlit as st
import requests

# CONFIGURATION
API_URL = "http://localhost:8000/chat"
st.set_page_config(page_title="Convolve AI", page_icon="🧠")

# --- HEADER ---
st.title("🧠 Convolve: Local AI Agent")
st.markdown("Chat with your **System Test Document** securely on your PC.")

# --- SESSION STATE (Memory for the UI) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT ---
if prompt := st.chat_input("Ask a question about your document..."):
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Call Backend API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            # Send request to FastAPI
            response = requests.post(API_URL, json={"query": prompt})
            
            if response.status_code == 200:
                answer = response.json().get("response", "No answer found.")
                message_placeholder.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                message_placeholder.error(f"Error: {response.status_code}")
        
        except Exception as e:
            message_placeholder.error(f"Connection Error: {e}")
            