from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    context.chat_data['marathons'] = ['марафон123..', ] # from DB
    context.chat_data['selected_now'] = 0

    reply_markup = ReplyKeyboardMarkup([[keyboards.PREV_BUTTON], [keyboards.BACK_BUTTON], [keyboards.NEXT_BUTTON]], resize_keyboard=True)
    update.message.reply_text(messages.MARATHON.format(
        context.chat_data['marathons'][context.chat_data['selected_now']]),
        reply_markup=reply_markup)


def prev_marathon(update: Update, context: CallbackContext):
    context.chat_data['selected_now'] -= 1
    if context.chat_data['selected_now'] < 0:
        context.chat_data['selected_now'] = len(context.chat_data['marathons']) - 1

    update.message.reply_text(messages.MARATHON.format(
        context.chat_data['marathons'][context.chat_data['selected_now']]))


def next_marathon(update: Update, context: CallbackContext):
    context.chat_data['selected_now'] += 1
    if context.chat_data['selected_now'] >= len(context.chat_data['marathons']):
        context.chat_data['selected_now'] = 0

    update.message.reply_text(messages.MARATHON.format(
        context.chat_data['marathons'][context.chat_data['selected_now']]))


marathons_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.NEXT_BUTTON})'), next_marathon),
        MessageHandler(Filters.regex(f'({keyboards.PREV_BUTTON})'), prev_marathon),
    ]
)
