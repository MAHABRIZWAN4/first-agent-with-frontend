# frontend.py
import streamlit as st
import asyncio
from main import get_ai_response  # backend function import kiya

st.set_page_config(page_title="Gemini Assistant", layout="centered")
st.title("🤖 Gemini 2.0 Assistant")

user_input = st.text_input("Ask me anything:")

if st.button("Submit") and user_input.strip():
    with st.spinner("Thinking..."):
        response = asyncio.run(get_ai_response(user_input))
        st.success("Answer:")
        st.write(response)





