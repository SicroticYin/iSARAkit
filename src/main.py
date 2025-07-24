import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_TOKEN"]

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from iSARAdev bot! 🪄 Hosted on Render.")

application.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.post(f"/{TOKEN}")
async def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "OK"

@app.get("/")
def index():
    return "iSARAdev bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)