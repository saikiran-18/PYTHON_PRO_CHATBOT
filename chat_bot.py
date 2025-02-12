import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import warnings

# Load environment variables
load_dotenv()

# Initialize the model
llM = ChatGroq(model="llama3-70b-8192")

# Streamlit title
st.title("PONG AI ((^◕ᴗ◕^))ChatBot")
st.caption("A conversational AI assistant powered by llama3-70b-8192b")
st.header("PYTHON PRO CHATBOT")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [

        SystemMessage( content=""""Hey there! I'm Pong, your friendly AI, here to help you conquer coding anxieties. ✨  SAI KIRAN built me to be your coding buddy!

Debugging can be tricky, but we'll get through it. Think of me as your guide.Practice makes perfect. Mistakes happen! You got this! ✨""")]


# Add some styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .user-message {
            color: white;
            background-color: #007bff;
            padding: 10px;
            border-radius: 10px;
            font-weight: bold;
            display: inline-block;
        }
        .ai-message {
            color: black;
            background-color: #e4e6eb;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)


# Chat input
query = st.chat_input("Enter your message ", key="query")

if query:
    try:
        # Add user message to history
        human_message = HumanMessage(content=query)
        st.session_state.chat_history.append(human_message)

        # Get AI response
        with st.spinner("DEBUGGING..ﮩ٨ﮩ٨ﮩ٨ﮩ٨ﮩ٨ﮩ٨ـ."):
            response = llM.invoke(st.session_state.chat_history)
            result = response.content

        if result:
            # Add AI response to history
            ai_message = AIMessage(content=result)
            st.session_state.chat_history.append(ai_message)

        # Display messages
        for message in st.session_state.chat_history:
            if isinstance(message, HumanMessage):
                st.markdown(f"<div class='user-message'>You:🍃 {message.content}</div>", unsafe_allow_html=True)
            elif isinstance(message, AIMessage):
                st.markdown(f"<div class='ai-message'>PYTHON PRO🪄✨Ai:{message.content}</div>", unsafe_allow_html=True)

        # Limit chat history length
        st.session_state.chat_history = st.session_state.chat_history[-100:]

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.markdown("<div class='ai-message'>ZenAi: Sorry, I encountered an error. Please try again.</div>", unsafe_allow_html=True)

# Optional: Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = [ SystemMessage(content=""""Hey there! I'm Pong, your friendly AI, here to help you conquer coding anxieties. ✨  SAI KIRAN built me to be your coding buddy!

Debugging can be tricky, but we'll get through it. Think of me as your guide.Practice makes perfect. Mistakes happen! You got this! ✨""" )]
    st.rerun()

warnings.filterwarnings("ignore")  # Generally not recommended