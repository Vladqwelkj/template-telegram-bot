from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext

from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    context.chat_data['is_need_comment_for_moderation'] = False
    reply_markup = ReplyKeyboardMarkup(keyboards.REJECT_APPROVE, resize_keyboard=True)

    for_moderation = 'для модерации...'

    update.message.reply_text(for_moderation, reply_markup=reply_markup)


def write_comment(update: Update, context: CallbackContext):
    context.chat_data['is_need_comment_for_moderation'] = True
    update.message.reply_text(messages.NEED_COMMENT_FOR_REJECT)


def to_main_menu(update: Update, context: CallbackContext):
    # одобряем то, что для модерации

    return names.MAIN_MENU


def comment_handler(update: Update, context: CallbackContext):
    if context.chat_data['is_need_comment_for_moderation']:
        del context.chat_data['is_need_comment_for_moderation']
        update.message.reply_text(messages.REJECT_IS_SENDED)

        comment = update.message.text
        # save comment 

        return names.MAIN_MENU



moderation_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.APPROVE_BUTTON})'), to_main_menu),
        MessageHandler(Filters.regex(f'({keyboards.REJECT_BUTTON})'), write_comment),
        MessageHandler(Filters.text, comment_handler),
    ]
)
