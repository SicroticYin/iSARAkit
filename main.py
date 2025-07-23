import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ.get("TELEGRAM_TOKEN")

app = Flask(__name__)

# Create Application instance WITHOUT polling or updater
application = Application.builder().token(TOKEN).build()

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from iSARAdev bot! 🪄 Hosted on Render.")

application.add_handler(CommandHandler("start", start))

# Webhook endpoint
@app.post(f"/{TOKEN}")
async def handle_update():
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "OK"

@app.get("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
