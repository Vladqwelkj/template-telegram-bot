from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    # Здесь должен быть просмотрщик отзывов, со стрелками.

    no_new_reviews = True

    if no_new_reviews:
        reply_markup = ReplyKeyboardMarkup(keyboards.BACK_KEYBOARD, resize_keyboard=True)
        update.message.reply_text(messages.NO_NEW_REVIEWS, reply_markup=reply_markup)


def reply_on_review(update: Update, context: CallbackContext):
    return names.REVIEW_REPLY


new_reviews_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.REPLY_BUTTON})'), reply_on_review)
    ]
)
