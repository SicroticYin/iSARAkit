import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = Flask(__name__)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

def start(update, context):
    update.message.reply_text("Hello! I'm alive and hosted on Render! 🚀")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)