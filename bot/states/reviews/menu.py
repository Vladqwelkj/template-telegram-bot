from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.REVIEWS_MENU, resize_keyboard=True)
    update.message.reply_text(messages.WHAT_TO_SEE, reply_markup=reply_markup)


def to_responsed(update: Update, context: CallbackContext):
    update.message.reply_text('# Бот присылает все отзывы')


def to_new_reviews(update: Update, context: CallbackContext):
    return names.REVIEWS_NEW


reviews_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.RESPONSED_BUTTON})'), to_responsed),
        MessageHandler(Filters.regex(f'({keyboards.NEW_BUTTON})'), to_new_reviews),
    ]
)
