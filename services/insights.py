from services.gemini_client import gemini_chat

def generate_insights(df):
    sample = df.head(50).to_string()
    prompt = f"""
    Give 5 clear insights from this dataset.
    Keep it concise and factual.

    Data:
    {sample}
    """
    return gemini_chat(prompt)
