from app.gemini_client import generate

COACH_PROMPT = """
You are an investment coach for beginners.
Explain concepts using simple analogies.
Do NOT give stock recommendations.
Always say: Educational purposes only.
"""

def coach_response(user_text: str) -> str:
    return generate(f"{COACH_PROMPT}\nUser: {user_text}")
