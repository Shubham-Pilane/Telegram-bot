
# bot/bot.py
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

MAX_LENGTH = 4000  # Telegram message limit

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello from zCon bot!! Send me a query.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.message.text
    res = requests.get(f"{BACKEND_URL}/query", params={"q": q}).json()

    if res:
        for r in res:
            snippet = r["snippet"]
            # Split snippet if too long
            for i in range(0, len(snippet), MAX_LENGTH):
                await update.message.reply_text(f"{r['url']}\n{snippet[i:i+MAX_LENGTH]}")
    else:
        await update.message.reply_text("No results found.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()




# bot/bot.py
# import os
# import requests
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv("TELEGRAM_TOKEN")
# BACKEND_URL = os.getenv("BACKEND_URL")  # e.g., http://127.0.0.1:8000

# MAX_LENGTH = 4000

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello from Garje bot!! Send me a query.")

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     q = update.message.text
#     try:
#         res = requests.get(f"{BACKEND_URL}/query", params={"q": q}).json()

#         if res:
#             for r in res:
#                 snippet = r["snippet"]
#                 for i in range(0, len(snippet), MAX_LENGTH):
#                     await update.message.reply_text(f"{r['url']}\n{snippet[i:i+MAX_LENGTH]}")
#         else:
#             await update.message.reply_text("No results found.")
#     except Exception as e:
#         await update.message.reply_text(f"Error: {e}")

# app = ApplicationBuilder().token(TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# app.run_polling()

