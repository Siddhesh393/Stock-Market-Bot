import os
import requests
from fastapi import FastAPI, Request

from app.router import route_message  # this now works

app = FastAPI()

TELEGRAM_URL = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}"

@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()

    if "message" not in data:
        return {"ok": True}

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    reply = route_message(text)

    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": reply,
            "parse_mode": "Markdown"
        }
    )

    return {"ok": True}
