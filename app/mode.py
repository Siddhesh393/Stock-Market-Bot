# In-memory mode storage (OK for serverless demo)
user_modes = {}

DEFAULT_MODE = "coach"

def set_mode(chat_id: int, mode: str):
    user_modes[chat_id] = mode

def get_mode(chat_id: int) -> str:
    return user_modes.get(chat_id, DEFAULT_MODE)
