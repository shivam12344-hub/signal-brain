import requests

BOT_TOKEN = "8470011841:AAGddLgbavit2oM4T9_L9dB8XHQn3w4wyR0"
CHAT_ID = "8563756627"

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    r = requests.post(url, json=payload, timeout=20)
    print("Telegram response:", r.status_code, r.text)
