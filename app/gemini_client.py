import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def generate(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
