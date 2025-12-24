from google import genai
from dotenv import load_dotenv
import os

# Load environment variables FIRST
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. "
        "Make sure .env exists in project root and contains GOOGLE_API_KEY."
    )

client = genai.Client(api_key=API_KEY)

def gemini_chat(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    return response.text
