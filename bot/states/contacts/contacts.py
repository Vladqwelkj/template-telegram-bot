from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.USERS, resize_keyboard=True)

    contacts = 'контакты123..'

    update.message.reply_text(messages.CONTACTS.format(contacts), reply_markup=reply_markup)


def users(update: Update, context: CallbackContext):
    pass

contacts_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.USERS_BUTTON})'), users),
    ]
)
