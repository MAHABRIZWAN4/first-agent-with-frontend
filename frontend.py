import streamlit as st
import asyncio
from main import get_ai_response

st.set_page_config(page_title="Gemini Pro Assistant", layout="centered", page_icon="✨")

# Custom CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Base Styles */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #f9fafb;
    color: #111827;
    line-height: 1.5;
}

/* Professional Gradient Background */
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
    z-index: -1;
}

/* Main Container */
.stApp {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2.5rem 3rem;
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(0, 0, 0, 0.05);
}

/* Header Section */
.header-container {
    text-align: center;
    margin-bottom: 2.5rem;
}

/* Title Styles */
.title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    text-fill-color: transparent;
    display: inline-block;
}

.subtitle {
    font-size: 1.1rem;
    font-weight: 400;
    color: #6b7280;
    margin-bottom: 0;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Input Field */
.stTextInput > div > input {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 14px 20px;
    font-size: 1rem;
    color: #111827;
    transition: all 0.2s ease;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.stTextInput > div > input:focus {
    border-color: #4f46e5;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
    outline: none;
}

.stTextInput > div > input::placeholder {
    color: #9ca3af;
}

/* Button Style */
.stButton > button {
    width: 100%;
    padding: 14px 0;
    border-radius: 12px;
    border: none;
    background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%);
    color: white;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
}

.stButton > button:active {
    transform: translateY(0);
}

/* Response Box */
.response-box {
    background: white;
    border: 1px solid #e5e7eb;
    padding: 24px;
    border-radius: 12px;
    margin-top: 2rem;
    font-size: 1rem;
    line-height: 1.7;
    color: #374151;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    white-space: pre-wrap;
    animation: fadeIn 0.3s ease-out;
}

/* Status Messages */
.stAlert {
    border-radius: 12px !important;
}

.stSpinner > div {
    justify-content: center;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 3rem;
    color: #9ca3af;
    font-size: 0.9rem;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .stApp {
        padding: 2rem 1.5rem;
        margin: 1rem;
    }
    .title {
        font-size: 2rem;
    }
}

/* Badge for Professional Look */
.pro-badge {
    display: inline-block;
    background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%);
    color: #fff !important;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
    vertical-align: middle;
    /* Remove background-clip and text-fill-color for solid white text */
    background-clip: border-box;
    -webkit-background-clip: border-box;
    -webkit-text-fill-color: #fff;
    text-fill-color: #fff;
}
</style>
""", unsafe_allow_html=True)

# UI Structure
st.markdown("""
<div class="header-container">
    <h1 class="title">Gemini Pro Assistant <span class="pro-badge">PRO</span></h1>
    <p class="subtitle">Enterprise-grade AI assistance with human-like understanding</p>
</div>
""", unsafe_allow_html=True)

# User Input
user_input = st.text_input("**Your question**", placeholder="How can I assist you today?")

# Response on Submit
if st.button("**Get Answer**") and user_input.strip():
    with st.spinner("Analyzing your request..."):
        response = asyncio.run(get_ai_response(user_input))
        st.success("Response generated")
        st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2023 Gemini Pro Assistant | Secure • Reliable • Enterprise-Ready
</div>
""", unsafe_allow_html=True)