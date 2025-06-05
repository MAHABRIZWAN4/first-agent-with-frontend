import streamlit as st
import asyncio
from main import get_ai_response

st.set_page_config(page_title="Gemini Assistant", layout="centered", page_icon="🤖")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

/* Background with dark blur + subtle animated neon shapes */
body, html, [class*="css"] {
    margin: 0; padding: 0; height: 100%;
    font-family: 'Poppins', sans-serif;
    background: #0f0f1a;
    overflow-x: hidden;
    color: #eee;
}

/* Animated neon blobs */
body::before {
    content: "";
    position: fixed;
    top: -20%;
    left: -20%;
    width: 140vw;
    height: 140vh;
    background:
      radial-gradient(circle at 30% 40%, #8e24aa88, transparent 50%),
      radial-gradient(circle at 70% 60%, #ff408188, transparent 60%),
      radial-gradient(circle at 50% 80%, #448aff88, transparent 60%);
    filter: blur(150px);
    animation: neonMove 30s infinite alternate ease-in-out;
    z-index: -1;
    opacity: 0.7;
}

@keyframes neonMove {
    0% {
        transform: translate(0, 0) scale(1);
    }
    50% {
        transform: translate(40px, 20px) scale(1.1);
    }
    100% {
        transform: translate(0, 0) scale(1);
    }
}

/* Main container - glassmorphism */
.stApp {
    max-width: 720px;
    margin: 3rem auto 4rem auto;
    padding: 2.5rem 3rem 3.5rem 3rem;
    background: rgba(30, 20, 50, 0.6);
    border-radius: 25px;
    box-shadow:
      0 8px 32px 0 rgba(98, 0, 234, 0.4),
      0 0 15px 3px rgba(138, 43, 226, 0.6);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1.5px solid rgba(138, 43, 226, 0.3);
    color: #eee;
}

/* Titles with neon glow */
.title {
    font-size: 4rem;
    font-weight: 900;
    text-align: center;
    color: #bb86fc;
    letter-spacing: 0.15em;
    text-shadow:
      0 0 8px #bb86fc,
      0 0 16px #bb86fc,
      0 0 24px #8a2be2;
    margin-bottom: 0.3em;
    animation: fadeUp 1.6s ease forwards;
}

.subtitle {
    font-size: 1.4rem;
    font-weight: 600;
    text-align: center;
    color: #d1c4e9cc;
    margin-bottom: 3.2rem;
    letter-spacing: 0.04em;
    animation: fadeUp 2.2s ease forwards;
}

/* Input box with glass + neon border and glow on focus */
.stTextInput > div > input {
    background: rgba(255, 255, 255, 0.05);
    border: 2px solid #8a2be2;
    border-radius: 16px;
    padding: 16px 22px;
    font-size: 1.2rem;
    color: #eee;
    transition: border-color 0.35s ease, box-shadow 0.35s ease;
    box-shadow: inset 0 0 12px #7b33d7aa;
    font-weight: 500;
    letter-spacing: 0.02em;
}

.stTextInput > div > input::placeholder {
    color: #b39ddb88;
    font-style: italic;
}

.stTextInput > div > input:focus {
    border-color: #bb86fc;
    box-shadow: 0 0 15px 3px #bb86fcaa, inset 0 0 20px #bb86fccc;
    outline: none;
    background: rgba(255, 255, 255, 0.1);
}

/* Button with gradient neon glow */
.stButton > button {
    width: 100%;
    max-width: 260px;
    margin: 0 auto;
    display: block;
    padding: 18px 0;
    border-radius: 25px;
    border: none;
    background: linear-gradient(45deg, #7f00ff, #e100ff);
    color: #fff;
    font-size: 1.3rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    cursor: pointer;
    box-shadow:
      0 0 10px #e100ff,
      0 0 25px #bb86fc;
    transition: background 0.4s ease, box-shadow 0.4s ease;
}

.stButton > button:hover {
    background: linear-gradient(45deg, #e100ff, #7f00ff);
    box-shadow:
      0 0 18px #e100ff,
      0 0 35px #bb86fc,
      0 0 45px #e100ff;
    color: #fff;
}

/* Response box with subtle neon border and shadow */
.response-box {
    background: rgba(50, 30, 70, 0.8);
    border-left: 6px solid #bb86fc;
    padding: 28px 32px;
    border-radius: 20px;
    margin-top: 45px;
    font-size: 1.2rem;
    line-height: 1.7;
    color: #e0d7ff;
    box-shadow:
      0 8px 25px rgba(187, 134, 252, 0.7);
    white-space: pre-wrap;
    animation: fadeUp 1.2s ease forwards;
}

/* Animations */
@keyframes fadeUp {
    0% {
        opacity: 0;
        transform: translateY(25px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# UI Structure
st.markdown("<div class='title'>🤖 Gemini 2.0 Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The sleek AI chatbot that feels futuristic</div>", unsafe_allow_html=True)

# User Input
user_input = st.text_input("💬 Ask me anything...", placeholder="Type your message here...")

# Response on Submit
if st.button("🚀 Submit") and user_input.strip():
    with st.spinner("🤖 Thinking..."):
        response = asyncio.run(get_ai_response(user_input))
        st.success("✅ Here's your answer:")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
