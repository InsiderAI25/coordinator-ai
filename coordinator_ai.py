import os
import requests
from flask import Flask

app = Flask(__name__)

# 🔐 Injected Bot Credentials
TELEGRAM_TOKEN = "7719709224:AAEQShc0d0Ol79rZLykcNyzXgB5WnGh214A"
CHAT_ID = "1194534732"

def send_startup_alert():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "🧠 Coordinator AI is now LIVE and responding on Telegram."
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Telegram alert sent:", response.json())
    else:
        print("❌ Failed to send Telegram alert:", response.status_code, response.text)

@app.route("/")
def home():
    send_startup_alert()
    return "✅ Coordinator AI is running and webhook is connected."

if __name__ == "__main__":
    print("🚀 Launching Coordinator AI Webhook...")
    app.run(host="0.0.0.0", port=10000)
