import duckduckgo

def bot_handler(event, context = None):
    if "message" not in event:
        return {}

    message = event["message"]
    chat_id = message["chat"]["id"]
    text = message["text"]

    prefix = "/ddg "
    if text.startswith(prefix):
        term = text[len(prefix):].strip()
        if term:
            text = duckduckgo.get_zci(term)
            return {"method": "sendMessage", "chat_id": chat_id, "text": text}

    return {}
