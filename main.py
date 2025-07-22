# main.py

import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

import os

# Optional if using in Jupyter or nested loops (not harmful elsewhere)
import nest_asyncio
nest_asyncio.apply()

# Replace with your bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Sample /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! iSARA Bot is running ✅")

# Main function to set up the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handler
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running... Press Ctrl+C to stop.")

    # Start the bot
    await app.run_polling()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
