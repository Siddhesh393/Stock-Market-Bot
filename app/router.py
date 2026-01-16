from app.safety import is_advice_request, refusal_message
from app.coach import coach_response
from app.market import market_response
from app.mode import get_mode, set_mode


def route_message(chat_id: int, text: str) -> str:
    text = text.strip().lower()

    # --- Mode Switching ---
    if text == "/mode coach":
        set_mode(chat_id, "coach")
        return (
            "🎓 *Coach Mode Activated*\n\n"
            "I’ll explain investing concepts using simple analogies.\n\n"
            "_Educational purposes only_"
        )

    if text == "/mode market":
        set_mode(chat_id, "market")
        return (
            "📰 *Market Commentary Mode Activated*\n\n"
            "I’ll provide neutral market summaries.\n\n"
            "_No investment advice_"
        )

    # --- Safety Guardrails ---
    if is_advice_request(text):
        return refusal_message()

    # --- Route Based on Mode ---
    mode = get_mode(chat_id)

    if mode == "market":
        return market_response(text)

    # Default: Coach mode
    return coach_response(text)
