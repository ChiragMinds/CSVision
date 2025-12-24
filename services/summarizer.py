from services.gemini_client import gemini_chat

def summarize_csv(text):
    prompt = f"Summarize the following CSV content:\n{text}"
    return gemini_chat(prompt)
