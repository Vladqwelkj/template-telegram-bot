from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.YES_NO, resize_keyboard=True)
    update.message.reply_text(messages.MSG_FOR_ALL.format(context.chat_data['current_message']),
        reply_markup=reply_markup)


def yes(update: Update, context: CallbackContext):
    # Отправляем сообщение пользователям
    return names.HELLO_HABIT_MENU

def no(update: Update, context: CallbackContext):
    # Отправляем сообщение пользователям
    return names.HELLO_HABIT_MENU


message_send_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.YES_BUTTON})'), yes),
        MessageHandler(Filters.regex(f'({keyboards.NO_BUTTON})'), no),
    ]
)
