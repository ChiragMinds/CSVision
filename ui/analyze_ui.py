import streamlit as st
from services.analyzer import analyze_dataframe
from services.gemini_client import gemini_chat

def analyze_ui(df):
    st.subheader("📈 Analyze CSV")

    question = st.chat_input("Ask an analytical question")
    if question:
        answer = analyze_dataframe(df, question, gemini_chat)
        st.chat_message("assistant").write(answer)
