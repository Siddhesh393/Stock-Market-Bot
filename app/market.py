from app.gemini_client import generate

MARKET_PROMPT = """
You are a neutral financial news commentator.
Summarize markets using macro, earnings, and global news.
No advice. No predictions.
"""

def market_response(user_text: str) -> str:
    return generate(f"{MARKET_PROMPT}\nUser: {user_text}")
