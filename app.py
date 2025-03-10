import streamlit as st
import ollama

# Streamlit UI
st.title("🤖 Mistral 7B Chatbot")
st.write("Type a message and click 'Generate' to get a response from Mistral.")

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # **Fix: Format messages correctly before sending to Ollama**
    formatted_messages = [{"role": msg["role"], "content": str(msg["content"])} for msg in st.session_state["messages"]]

    # Generate response from Mistral
    response = ollama.chat(model="mistral", messages=formatted_messages)
    bot_message = response["message"]

    # Display bot response
    st.session_state["messages"].append({"role": "assistant", "content": bot_message})
    with st.chat_message("assistant"):
        st.write(bot_message)
