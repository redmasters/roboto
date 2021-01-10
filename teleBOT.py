import logging
import telegram
from telegram.ext import Updater
from telegram.ext import dispatcher
from telegram.ext.commandhandler import CommandHandler
from telegram.ext import MessageHandler, Filters

bot = telegram.Bot(token="893162503:AAGwD5FvkRYYs297kEMkI_wvI0gdbaG6p7Y")
updater = Updater(
    token="893162503:AAGwD5FvkRYYs297kEMkI_wvI0gdbaG6p7Y", use_context=True
)
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Envia uma resposta ao receber o comando /start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Falaa jovem, qual a QTC?"
    )


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)


# Repete as mensagens digitadas no bot após o comando /start
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Formata as mensagens em caixa alta (CAPS-LOCK)
def caps(update, context):
    text_caps = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler("caps", caps)
dispatcher.add_handler(caps_handler)


updater.start_polling()
