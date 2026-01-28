import streamlit as st
import time

# --- PROJECT: NEXUS-AI LOGIC ENGINE (TASK 1) ---
st.set_page_config(page_title="Nexus-AI Assistant", page_icon="⚡", layout="wide")

with st.sidebar:
    st.title("👤 Developer")
    st.markdown("""
    **Name:** Darshan Kotadiya  
    Role: MERN Stack & AI Research Intern
    
    [🔗 LinkedIn](https://www.linkedin.com/in/darshankotadiya)  
    [📂 GitHub](https://github.com/darshankotadiya/CODSOFT)
    """)
    st.divider()
    st.info("Supported Commands: 'Who are you?', 'MERN Stack', 'System Status', 'EduSmart Project'")

st.title("⚡ Nexus-AI: Rule-Based Logic Assistant")
st.write("---")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_logic_response(user_input):
    query = user_input.lower().strip()
    
    if any(x in query for x in ["who are you", "identity", "name"]):
        return "I am Nexus-AI, a rule-based logic engine developed by Darshan for CodSoft."
    
    elif any(x in query for x in ["darshan", "mern", "creator"]):
        return "Darshan is a MERN Stack Developer specializing in AI integrations and scalable web apps."
    
    elif "edusmart" in query or "project" in query:
        return "The creator is currently building 'EduSmart-Pro AI', a next-gen LMS due in March 2026."
    
    elif any(x in query for x in ["how are you", "status", "health"]):
        return "Operational status: 100%. All rule-based logic gates are functioning optimally."
    
    elif any(x in query for x in ["hi", "hello", "hey"]):
        return "Hello! I am Nexus-AI. Please enter a command to trigger my logic gates."
    
    elif any(x in query for x in ["bye", "exit", "quit"]):
        return "Terminating session. Have a productive day ahead!"
    
    else:
        return "Command unrecognized. Please consult the sidebar for a list of supported logic triggers."

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if prompt := st.chat_input("Enter logic command..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        time.sleep(0.4)
        response = get_logic_response(prompt)
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
