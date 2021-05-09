import os
from dotenv import load_dotenv

load_dotenv() 
TOKEN = os.getenv("TOKEN")

from telegram.ext import *
from router import route

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
updater.start_polling()

print("Your telegram bot is running!")

updater.idle()


