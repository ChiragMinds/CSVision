def analyze_dataframe(df, question, llm_call):
    context = df.head(50).to_string()
    prompt = f"""
    Given this dataframe:
    {context}

    Answer this:
    {question}
    """
    return llm_call(prompt)
