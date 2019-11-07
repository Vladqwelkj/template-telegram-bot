from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext, MessageHandler, Filters

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    context.chat_data['is_hello_habit_way'] = True
    context.chat_data['is_organisator_way'] = False
    reply_markup = ReplyKeyboardMarkup(keyboards.HELLO_HABIT_MENU, resize_keyboard=True)
    update.message.reply_markdown(messages.WHAT_TO_SEE, reply_markup=reply_markup)


def to_analytics(update: Update, context: CallbackContext):
    return names.ANALYTICS_MENU

def to_reviews(update: Update, context: CallbackContext):
    return names.REVIEWS_MENU

def to_contacts(update: Update, context: CallbackContext):
    return names.CONTACTS_MENU

def to_message(update: Update, context: CallbackContext):
    return names.MESSSAGE_WRITE




hello_habit_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.ANALYTICS_BUTTON})'), to_analytics),
        MessageHandler(Filters.regex(f'({keyboards.REVIEWS_BUTTON})'), to_reviews),
        MessageHandler(Filters.regex(f'({keyboards.CONTACTS_BUTTON})'), to_contacts),
        MessageHandler(Filters.regex(f'({keyboards.MESSAGE_BUTTON})'), to_message),
            ]
)
