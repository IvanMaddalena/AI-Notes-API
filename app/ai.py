import os
import httpx
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def summarize_note_with_ai(content: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral/mistral-7b-instruct",  # Puoi cambiarlo
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes notes."},
            {"role": "user", "content": f"Summarize this note: {content}"}
        ],
        "max_tokens": 300
    }

    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error during summarization: {str(e)}"
