import streamlit as st
from services.profiling import profile_dataframe

def profile_ui(df):
    st.subheader("📊 Dataset Overview")

    profile = profile_dataframe(df)

    st.subheader("Statistical Summary")
    st.dataframe(profile["describe"])

    col1, col2 = st.columns(2)
    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])

    st.subheader("Missing Values")
    st.dataframe(profile["missing"])

    st.subheader("Data Types")
    st.dataframe(profile["dtypes"])

