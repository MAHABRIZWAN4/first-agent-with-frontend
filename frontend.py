import streamlit as st
import asyncio
from main import get_ai_response

# Page config
st.set_page_config(page_title="Gemini Assistant", layout="centered", page_icon="🤖")

# Custom CSS with animations and fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #e0f7fa, #e1bee7);
        color: #333;
    }

    .title {
        text-align: center;
        font-size: 3.5em;
        font-weight: 700;
        color: #6a1b9a;
        text-shadow: 2px 2px 5px rgba(106, 27, 154, 0.3);
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    .subtitle {
        text-align: center;
        color: #424242;
        font-size: 1.2em;
        margin-bottom: 40px;
        animation: fadeIn 2.5s ease-in-out;
    }

    .stTextInput input {
        background-color: #ffffffdd;
        border: 2px solid #6a1b9a;
        border-radius: 12px;
        padding: 10px;
        font-size: 1em;
        transition: 0.3s;
    }

    .stTextInput input:focus {
        border-color: #ab47bc;
        box-shadow: 0 0 0 0.2rem rgba(171, 71, 188, 0.25);
    }

    .stButton>button {
        background-color: #6a1b9a;
        color: white;
        border-radius: 10px;
        font-size: 1em;
        padding: 10px 30px;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #8e24aa;
        color: #fff;
    }

    .response-box {
        background-color: #f3e5f5;
        border-left: 5px solid #6a1b9a;
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px;
        animation: fadeIn 1s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# UI Structure
st.markdown("<div class='title'>🤖 Gemini 2.0 Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your stylish AI chatbot powered by Streamlit</div>", unsafe_allow_html=True)

# User Input
user_input = st.text_input("💬 Type your message here:")

# Response on Submit
if st.button("🚀 Submit") and user_input.strip():
    with st.spinner("🤔 Thinking..."):
        response = asyncio.run(get_ai_response(user_input))
        st.success("✅ Answer:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
