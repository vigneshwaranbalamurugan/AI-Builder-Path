import requests

from dotenv import load_dotenv
import os
load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
def create_embedding(text):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )

    return response.json()["embedding"]