import os
import requests
from fastapi import FastAPI, Request

from app.router import route_message

app = FastAPI()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()

        if "message" not in data:
            return {"ok": True}

        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = route_message(chat_id, text)

        requests.post(
            f"{TELEGRAM_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            },
            timeout=10
        )

        return {"ok": True}

    except Exception as e:
        print("Webhook error:", str(e))
        return {"ok": True}
