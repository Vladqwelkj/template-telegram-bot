from datetime import datetime, timedelta

from telegram import Update, ReplyKeyboardMarkup, Bot
from telegram.ext import MessageHandler, Filters, CallbackContext, CallbackQueryHandler

from bot.utils import get_analytics, send_analytics
from bot.utils.calendar_keyboard import CalendarKeyboard
from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State



def activator(update: Update, context: CallbackContext):
    context.chat_data['selected_date_end'] = False
    CalendarKeyboard(context).clear_context_data()
    _send_calendar(update, context, message=messages.DATE_END)


def done(update: Update, context: CallbackContext):
    return names.MAIN_MENU


def select_confirmation(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup([[keyboards.DONE_BUTTON], [keyboards.COMPARE_BUTTON], [keyboards.CANCEL_BUTTON]])
    update.message.reply_text(messages.PERIOD_IS_SELECTED, reply_markup=reply_markup)

    if context.chat_data['selected_date_end'] and context.chat_data['selected_date_start']:
        if context.chat_data['is_hello_habit_way']:
            result = get_analytics.hello_habit(update.message.from_user.id,
                                               context.chat_data['selected_date_start'],
                                               context.chat_data['selected_date_end'],
                                               )
            send_analytics.hello_habit(update, result)
        if context.chat_data['is_organisator_way']:
            pass


def to_compare(update: Update, context: CallbackContext):
    return names.SELECT_START_DATE_FOR_COMPARE




def process_calendar(update: Update, context: CallbackContext):
    calendar = CalendarKeyboard(context, allow_past=True)

    if calendar.is_valid_monthday(update.message.text):
        reply_markup = ReplyKeyboardMarkup([[keyboards.SELECT_BUTTON], [keyboards.CANCEL_BUTTON]])
        update.message.reply_text(str(calendar.get_monthday_date(update.message.text)), reply_markup=reply_markup)
        context.chat_data['selected_date_end'] = calendar.get_monthday_date(update.message.text)


    elif calendar.is_valid_month_name(update.message.text):
        calendar.change_month(update.message.text)
        _send_calendar(update, context)

    else:
        update.message.reply_text(messages.INCORRECT_INPUT)


def _send_calendar(update: Update, context: CallbackContext, message='Выберите дату'):
    calendar = CalendarKeyboard(context, allow_past=True)

    current_month = calendar.get_current_month_name()
    current_year = calendar.get_current_year()

    keyboard = calendar.get_keyboard(footer=[[keyboards.CANCEL_BUTTON]])

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)


select_end_date_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.CANCEL_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.SELECT_BUTTON})'), select_confirmation),
        MessageHandler(Filters.regex(f'({keyboards.DONE_BUTTON})'), done),
        MessageHandler(Filters.regex(f'({keyboards.CANCEL_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.COMPARE_BUTTON})'), to_compare),
        MessageHandler(Filters.text, process_calendar),
    ]
)


