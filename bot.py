import requests
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from dotenv import load_dotenv
load_dotenv()
import os
TELEGRAM_TOKEN = os.environ.get("BOT_TOKEN")

updater = Updater(TELEGRAM_TOKEN,
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello, Welcome to the Bot.Please write\
        /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text('Send a link to see if the website is up or down')


def messaging(update: Update, context: CallbackContext):
    url = update.message.text
    try:
        response = requests.head(url)
    except Exception as e:
        update.message.reply_text(f"NOT OK: {str(e)}")
    else:
        if response.status_code == 200:
            update.message.reply_text("This link runs ok")
        else:
            update.message.reply_text(f"NOT OK: HTTP response code {response.status_code}")
    update.message.reply_text



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, messaging))
updater.start_polling()