import streamlit as st
from services.csv_loader import load_csv
from services.vector_store import build_faiss
from services.insights import generate_insights
from ui.chat_ui import chat_ui
from ui.summary_ui import summary_ui
from ui.analyze_ui import analyze_ui
from ui.profile_ui import profile_ui

st.set_page_config("CSVision", layout="wide")
st.title("🧠 CSVision")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = load_csv(uploaded_file)
    texts = df.astype(str).apply(" ".join, axis=1).tolist()
    index, _ = build_faiss(texts)

    feature = st.selectbox(
        "Choose a feature",
        ["Profile", "Chat", "Summarize", "Analyze", "Insights"]
    )

    if feature == "Profile":
        profile_ui(df)

    elif feature == "Chat":
        chat_ui(df, texts, index)

    elif feature == "Summarize":
        summary_ui("\n".join(texts[:50]))

    elif feature == "Analyze":
        analyze_ui(df)

    elif feature == "Insights":
        if st.button("⚡ Generate Insights"):
            st.success(generate_insights(df))
else:
    st.info("Upload a CSV to begin")
