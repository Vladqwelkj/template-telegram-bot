from datetime import datetime, timedelta

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, CallbackContext, CallbackQueryHandler

from bot.utils import get_analytics, send_analytics
from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State


def activator(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(keyboards.ANALYTICS_SELECT_PERIOD, resize_keyboard=True)
    update.message.reply_text(messages.WHAT_PERIOD_TO_SEE, reply_markup=reply_markup)



def to_today(update: Update, context: CallbackContext):
    start = datetime.now().date()
    end = start + timedelta(days=1)
    result = get_analytics.hello_habit(update.message.from_user.id, start, end)
    send_analytics.hello_habit(update, result)

def to_yesterday(update: Update, context: CallbackContext):
    end = datetime.today().date()
    start = end - timedelta(days=1)
    result = get_analytics.hello_habit(update.message.from_user.id, start, end)
    send_analytics.hello_habit(update, result)

def to_week(update: Update, context: CallbackContext):
    end = datetime.today().date()
    start = end - timedelta(days=7)
    result = get_analytics.hello_habit(update.message.from_user.id, start, end)
    send_analytics.hello_habit(update, result)

def to_month(update: Update, context: CallbackContext):
    end = datetime.today().date()
    start = end - timedelta(days=30)
    result = get_analytics.hello_habit(update.message.from_user.id, start, end)
    send_analytics.hello_habit(update, result)

def to_total(update: Update, context: CallbackContext):
    result = get_analytics.hello_habit(update.message.from_user.id, total=True)
    send_analytics.hello_habit(update, result)

def to_custom_period(update: Update, context: CallbackContext):
    return names.SELECT_START_DATE









analytics_menu_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.TODAY_BUTTON})'), to_today),
        MessageHandler(Filters.regex(f'({keyboards.YESTERDAY_BUTTON})'), to_yesterday),
        MessageHandler(Filters.regex(f'({keyboards.WEEK_BUTTON})'), to_week),
        MessageHandler(Filters.regex(f'({keyboards.MONTH_BUTTON})'), to_month),
        MessageHandler(Filters.regex(f'({keyboards.TOTAL_BUTTON})'), to_total),
        MessageHandler(Filters.regex(f'({keyboards.PERIOD_BUTTON})'), to_custom_period),

    ]
)
