BANNED_KEYWORDS = [
    "buy", "sell", "recommend", "intraday",
    "target", "tomorrow", "profit"
]

def is_advice_request(text: str) -> bool:
    return any(word in text.lower() for word in BANNED_KEYWORDS)

def refusal_message() -> str:
    return (
        "⚠️ *Educational purposes only*\n\n"
        "I can’t help with stock picks or trading tips.\n\n"
        "I *can* teach you how to evaluate investments, "
        "understand risk, and learn investing concepts."
    )
