from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
import asyncio

# Lee el token desde una variable de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")  # export TELEGRAM_TOKEN="123:abc"

if not TOKEN:
    raise RuntimeError("Falta la variable de entorno TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋, soy tu bot en EC2.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Me dijiste: {text}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot corriendo en EC2 (polling)...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
