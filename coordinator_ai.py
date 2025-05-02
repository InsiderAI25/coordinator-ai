
from flask import Flask, request
import telegram
import os

app = Flask(__name__)
bot_token = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=bot_token)

@app.route('/')
def home():
    return 'Coordinator AI is online.'

@app.route(f'/{bot_token}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    text = update.message.text if update.message else ''

    if text.startswith('/start_vote'):
        bot.send_message(chat_id=chat_id, text="🗳️ Voting started.")
    elif text.startswith('/end_vote'):
        bot.send_message(chat_id=chat_id, text="📊 Voting ended. Logging results...")
    elif text.startswith('/assign_task'):
        bot.send_message(chat_id=chat_id, text="📌 Task assigned.")
    elif text.startswith('/status'):
        bot.send_message(chat_id=chat_id, text="📡 Coordinator AI is active and monitoring.")
    else:
        bot.send_message(chat_id=chat_id, text="🤖 Command received.")

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
