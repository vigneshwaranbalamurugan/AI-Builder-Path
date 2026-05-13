import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("API KEY:", GEMINI_API_KEY)
genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-3-flash-preview"
)

def generate(prompt):

    response = model.generate_content(
        prompt
    )

    return response.text