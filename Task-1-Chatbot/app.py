
import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Nexus-AI Assistant", page_icon="🤖")

st.title("🤖 Nexus-AI: Rule-Based Assistant")
st.markdown("Developed by **Darshan** for CodSoft Internship")

# Initializing Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Logic function (Your existing logic)
def get_bot_response(user_input):
    query = user_input.lower()
    if "hello" in query or "hi" in query:
        return "Greetings! I am Nexus-AI. How can I help you today?"
    elif "your name" in query:
        return "I am a Rule-based AI developed by Darshan for CodSoft."
    elif "mern" in query:
        return "My creator is a MERN Stack expert, currently building EduSmart-Pro AI!"
    elif "bye" in query:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, my current logic-gate is limited. Could you rephrase?"

# Displaying chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Bot Response
    response = get_bot_response(prompt)
    time.sleep(0.5) # Fake latency for realism
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
