import streamlit as st
import ollama
st.title("Ollama Chatbot")
# st.session_state is stresmlit's way of remembering covo
#message is a list that stores convo history
if "messages" not in st.session_state: 
    st.session_state.messages = []

#displayprevious messages
# message[role] either u or assistant
# message["content"] is the actual text message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# to get user input
# st.chat_input creates a text box at the bottom
#prompt stores what u type
if prompt := st.chat_input("Ask me something!"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # ollama.chat sens convo to LLaMa3
    #model.lllama3 tells which AI model to use
    #messages=st.session_state.messages sends convo history
    #reply=response["message"]["content"] extracts just the text from LLaMA's response
    # st.markdown(reply) shows bot's answer on screen 
    with st.chat_message("assistant"):
        response=ollama.chat(model="llama3", messages=st.session_state.messages)
        reply=response["message"]["content"]
        st.markdown(reply)

    # adds the bot's reply to memory. now both your and bot's answers are saved for context in next message
    st.session_state.messages.append({"role":"assistant","content":reply})