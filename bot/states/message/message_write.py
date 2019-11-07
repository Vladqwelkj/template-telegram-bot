from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.LOG, resize_keyboard=True)
    update.message.reply_text(messages.WRITE_MSG, reply_markup=reply_markup)

def send_log(update: Update, context: CallbackContext):
    return names.MESSAGE_LOG

def make_message(update: Update, context: CallbackContext):
    context.chat_data['current_message'] = update.message.text

    #Здесь сообщение сохраняется. Ниже  спрашивает, отправить ли всем пользователям?

    return names.MESSAGE_SEND


messsage_write_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.LOG_BUTTON})'), send_log),
        MessageHandler(Filters.text, make_message),
    ]
)
