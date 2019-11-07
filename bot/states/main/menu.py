from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from extensions import State

from bot.states.common import back

def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.MAIN_MENU, resize_keyboard=True)
    update.message.reply_text(messages.MAIN_MENU, reply_markup=reply_markup)

def to_hello_habit_menu(update: Update, context: CallbackContext):
    return names.HELLO_HABIT_MENU

def to_organisator_menu(update: Update, context: CallbackContext):
    return names.ORGANISATOR_MENU


main_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.HELLO_HABIT_BUTTON})'), to_hello_habit_menu),
        MessageHandler(Filters.regex(f'({keyboards.ORGANISATOR_BUTTON})'), to_organisator_menu),
    ]
)
