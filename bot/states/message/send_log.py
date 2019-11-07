from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.BACK_KEYBOARD, resize_keyboard=True)

    log_str = 'some log123...'

    update.message.reply_text(messages.MSG_LOG.format(log_str), reply_markup=reply_markup)




message_log_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
    ]
)
