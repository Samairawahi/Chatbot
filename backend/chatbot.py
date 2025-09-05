
import os, requests
from dotenv import load_dotenv
from personas import PERSONAS

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError(" GOOGLE_API_KEY not found in .env")

def build_system_instruction(persona: str):
    """Return system instruction text based on persona."""
    return {
        "role": "system",
        "parts": [{"text": PERSONAS.get(persona, PERSONAS["farmer"])}]
    }

def get_chatbot_response(prompt: str, persona: str = "farmer") -> str:
    """Call Gemini API and return chatbot response text."""
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": API_KEY}

    data = {
        "system_instruction": build_system_instruction(persona),
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 200}
    }

    try:
        response = requests.post(url, headers=headers, params=params, json=data, timeout=60)
        resp_json = response.json()
        return resp_json["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"Chatbot service error: {str(e)}"

