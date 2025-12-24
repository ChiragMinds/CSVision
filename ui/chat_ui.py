import streamlit as st
import pandas as pd
from services.vector_store import retrieve
from services.gemini_client import gemini_chat

def chat_ui(df, texts, index):

    st.subheader("💬 Chat with CSV")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    suggestions = [
        "What columns are present?",
        "Which column has missing values?",
        "Give a summary of numeric columns",
        "What trends do you see?"
    ]

    st.caption("Suggested questions:")
    for q in suggestions:
        if st.button(q):
            st.session_state.user_query = q

    column_focus = st.selectbox(
        "Optional: Focus on a column",
        ["None"] + list(df.columns)
    )

    query = st.chat_input("Ask a question about your CSV")

    if query:
        docs = retrieve(query, texts, index)
        context = "\n".join(docs)

        if column_focus != "None":
            context += f"\n\nFocus ONLY on column `{column_focus}`:\n"
            context += df[column_focus].head(20).to_string()

        answer = gemini_chat(
            f"Context:\n{context}\n\nQuestion:\n{query}"
        )

        st.session_state.chat_history.append(
            {"question": query, "answer": answer}
        )

        st.chat_message("assistant").write(answer)

    if st.session_state.chat_history:
        st.download_button(
            "⬇ Download Chat History",
            pd.DataFrame(st.session_state.chat_history).to_csv(index=False),
            "chat_history.csv"
        )
