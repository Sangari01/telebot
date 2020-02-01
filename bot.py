
#imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

#variables
updater = Updater(token='963151855:AAE1nFV9VMe8fciU_pDBys34E0udtvPPR4I', use_context=True)
dispatcher = updater.dispatcher

#functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vanakkam Neyergele")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def SetDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")

def Raasi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")

#Main
start_handler = CommandHandler('Start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

Date_handler = CommandHandler('SetDate', SetDate)
dispatcher.add_handler(Date_handler)

Raasi_handler = CommandHandler('Raasi', Raasi)
dispatcher.add_handler(Raasi_handler)


updater.start_polling()
print('Bot is working')