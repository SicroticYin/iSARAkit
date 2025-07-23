import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Load environment variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Create Flask app
app = Flask(__name__)

# Define the command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m alive and hosted on Render! 🚀")

# Create Application instance (new way to handle Telegram bot)
application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# Set up webhook endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook() -> str:
    """Webhook endpoint that receives updates from Telegram"""
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "OK"

# Health check route
@app.route("/")
def health_check():
    return "Bot is running!"

# Start Flask server
if __name__ == "__main__":
    app.run(port=5000)
