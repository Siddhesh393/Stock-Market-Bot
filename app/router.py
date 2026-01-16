from app.safety import is_advice_request, refusal_message
from app.coach import coach_response
from app.market import market_response


def route_message(text: str) -> str:
    text = text.strip().lower()

    # --- Session / Command Handling ---
    if text in ["/start"]:
        return (
            "👋 *Welcome to Investment Coach Bot*\n\n"
            "I help you:\n"
            "• Learn investing concepts (Beginner → Intermediate)\n"
            "• Understand market news in a neutral way\n\n"
            "⚠️ *Educational purposes only*\n"
            "I do NOT provide stock tips or buy/sell recommendations.\n\n"
            "Type `/help` to see what I can do."
        )

    if text in ["/help"]:
        return (
            "ℹ️ *How I can help*\n\n"
            "📘 *Investment Coach*\n"
            "• Stocks, ETFs, SIPs, Risk\n"
            "• Explained with simple analogies\n\n"
            "📰 *Market Commentary*\n"
            "• Why markets moved today\n"
            "• Macro & news-based summaries\n\n"
            "🚫 I cannot give:\n"
            "• Stock picks\n"
            "• Intraday tips\n"
            "• Guaranteed returns\n\n"
            "Type `/end` to finish the session.\n"
            "_Educational purposes only_"
        )

    if text in ["/end", "/stop", "/quit"]:
        return (
            "👋 *Session ended*\n\n"
            "You can come back anytime to learn about investing or "
            "understand market news.\n\n"
            "_Educational purposes only_"
        )

    # --- Safety Guardrails (Highest Priority) ---
    if is_advice_request(text):
        return refusal_message()

    # --- Market Commentary Mode ---
    if any(keyword in text for keyword in ["market", "today", "news", "sensex", "nifty"]):
        return market_response(text)

    # --- Default: Investment Coach Mode ---
    return coach_response(text)
