from tkinter import PhotoImage
from telegram import Bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from CoinBase import CMC_df
import dataframe_image as dfi
from telegram.ext.inlinequeryhandler import InlineQueryHandler
from telegram import ParseMode


# initializing the bot with API
bot = Bot("5422958978:AAGaoowQjrHa312Mcl0wD3qzFOMDGkNbQOk")
updater = Updater("5422958978:AAGaoowQjrHa312Mcl0wD3qzFOMDGkNbQOk",
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Get scrapped cryto data from multiple sources and insight into the hottest info")
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize what you said '%s'" % update.message.text)

  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def new(update: Update, context: CallbackContext):
    try:
        chat_id = update.message.chat_id
        update.message.reply_text(f'<pre>{CMC_df}</pre>', parse_mode=ParseMode.HTML )
        
        
    except:
        update.message.reply_text("something went wrong."
            )


#adding handlers to for the messages
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('new', new))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


# getting the bot details
print(bot.get_me())

updater.start_polling()
updater.idle()