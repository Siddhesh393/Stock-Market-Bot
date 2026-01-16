from app.gemini_client import generate

MARKET_PROMPT = """
You are a neutral financial market commentator.
Explain market movements using macroeconomic factors,
earnings trends, interest rates, and global news.
No advice. No predictions. No stock recommendations.
"""


def market_response(user_text: str) -> str:
    return generate(f"{MARKET_PROMPT}\nUser: {user_text}")
