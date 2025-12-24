import streamlit as st
from services.summarizer import summarize_csv

def summary_ui(text):
    if st.button("📝 Generate Summary"):
        with st.spinner("Summarizing..."):
            st.success(summarize_csv(text))
