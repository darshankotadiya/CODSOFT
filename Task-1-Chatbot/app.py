import streamlit as st
import time

# =================================================================
# PROJECT: NEURAL-LOGIC RULE-BASED CHATBOT (TASK 1)
# DEVELOPER: DARSHAN KOTADIYA
# INTERNSHIP: CODSOFT AI
# =================================================================

# Page Configuration for a professional look
st.set_page_config(page_title="Nexus-AI Assistant", page_icon="🤖", layout="wide")

# --- SIDEBAR: INSTRUCTIONS & ABOUT ---
with st.sidebar:
    st.title("👤 Developer Profile")
    st.markdown("""
    **Name:** Darshan Kotadiya  
    **Role:** MERN Stack & AI Research Intern  
    
    [LinkedIn Profile](https://www.linkedin.com/in/darshan-kotadiya-70416a251/)  
    [GitHub Repository](https://github.com/darshankotadiya/CODSOFT)
    """)
    
    st.divider()
    
    st.title("📖 How to Interact?")
    st.info("""
    Since this is a **Rule-Based AI**, please use the following keywords for the best experience:
    - **Greetings:** 'Hello', 'Hi', 'Hey'
    - **Identity:** 'Who are you?', 'Your name?'
    - **Capabilities:** 'What can you do?'
    - **Status:** 'How are you?'
    - **Tech Info:** 'MERN', 'Project'
    - **Exit:** 'Bye', 'Quit', 'Exit'
    """)
    
    st.success("Tip: This bot uses pattern matching to identify user intent!")

# --- MAIN CHAT INTERFACE ---
st.title("🤖 Nexus-AI: Professional Rule-Based Assistant")
st.caption("A CodSoft Internship Project - Task 1")

# Initializing Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Core Logic Function (Rule-Based Pattern Matching)
def get_bot_response(user_input):
    query = user_input.lower().strip()
    
    # Matching logic
    if any(word in query for word in ["hello", "hi", "hey", "greetings"]):
        return "Greetings! I am Nexus-AI. How can I assist your workflow today?"
    
    elif "who are you" in query or "name" in query or "identity" in query:
        return "I am Nexus-AI, a rule-based engine developed by Darshan for the CodSoft Internship."
    
    elif "how are you" in query or "status" in query:
        return "System status: Healthy. Latency: Minimal. I am functioning at peak efficiency!"
    
    elif "what can you do" in query or "capabilities" in query:
        return "I can execute predefined logic gates, recognize language patterns, and provide internship metadata."
    
    elif "mern" in query or "project" in query:
        return "My creator, Darshan, is a MERN Stack expert currently building 'EduSmart-Pro AI'!"
    
    elif any(word in query for word in ["bye", "exit", "quit"]):
        return "Deactivating session. Thank you for the interaction. Have a productive day!"
    
    else:
        return "Query unrecognized. Please refer to the sidebar for supported keywords."

# Displaying Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Interaction Input
if prompt := st.chat_input("Enter your command here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display response
    response = get_bot_response(prompt)
    time.sleep(0.4) # Simulating processing time
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
