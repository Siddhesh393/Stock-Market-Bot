from app.safety import is_advice_request, refusal_message
from app.coach import coach_response
from app.market import market_response
from app.mode import get_mode, set_mode


def route_message(chat_id: int, text: str) -> str:
    raw_text = text.strip()
    text = raw_text.lower()

    # =========================
    # START / HELP COMMANDS
    # =========================
    if text == "/start":
        set_mode(chat_id, "coach")  # default mode
        return (
            "👋 *Welcome to Investment Coach Bot*\n\n"
            "I help you:\n"
            "• Learn investing concepts (Beginner → Intermediate)\n"
            "• Understand market news in a neutral way\n\n"
            "⚠️ *Educational purposes only*\n"
            "I do NOT provide stock tips or buy/sell recommendations.\n\n"
            "Use:\n"
            "`/mode coach` – Investment learning\n"
            "`/mode market` – Market commentary\n\n"
            "Type `/help` to see what I can do."
        )

    if text == "/help":
        return (
            "ℹ️ *How I can help*\n\n"
            "🎓 *Coach Mode*\n"
            "• Stocks, ETFs, SIPs, Risk\n"
            "• Explained using simple analogies\n\n"
            "📰 *Market Commentary Mode*\n"
            "• Why markets moved today\n"
            "• Neutral news-style summaries\n\n"
            "🚫 I cannot:\n"
            "• Recommend stocks\n"
            "• Give intraday tips\n"
            "• Promise guaranteed returns\n\n"
            "Switch modes using:\n"
            "`/mode coach`\n"
            "`/mode market`\n\n"
            "_Educational purposes only_"
        )

    # =========================
    # MODE SWITCHING
    # =========================
    if text == "/mode coach":
        set_mode(chat_id, "coach")
        return (
            "🎓 *Coach Mode Activated*\n\n"
            "Ask me about stocks, ETFs, SIPs, risk, and investing basics.\n\n"
            "_Educational purposes only_"
        )

    if text == "/mode market":
        set_mode(chat_id, "market")
        return (
            "📰 *Market Commentary Mode Activated*\n\n"
            "Ask me about today’s market movement or news.\n\n"
            "_No investment advice_"
        )

    # =========================
    # SAFETY GUARDRAILS
    # =========================
    if is_advice_request(text):
        return refusal_message()

    # =========================
    # ROUTE BY MODE
    # =========================
    mode = get_mode(chat_id)

    if mode == "market":
        return market_response(raw_text)

    # Default → Coach Mode
    return coach_response(raw_text)
