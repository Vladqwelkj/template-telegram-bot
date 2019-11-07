from datetime import datetime, timedelta

from telegram import Update, ReplyKeyboardMarkup, Bot
from telegram.ext import MessageHandler, Filters, CallbackContext, CallbackQueryHandler

from bot.utils.calendar_keyboard import CalendarKeyboard
from bot.resources import keyboards, messages
from bot.states import names
from bot.states.common import back
from extensions import State



def activator(update: Update, context: CallbackContext):
    context.chat_data['selected_date_start_for_compare'] = False
    

    CalendarKeyboard(context).clear_context_data()
    _send_calendar(update, context, message=messages.DATE_START_SECOND)



def show_calendar(update: Update, context: CallbackContext):
    CalendarKeyboard(context).clear_context_data()
    _send_calendar(update, context)


def process_calendar(update: Update, context: CallbackContext):
    calendar = CalendarKeyboard(context, allow_past=True)

    if calendar.is_valid_monthday(update.message.text):
        update.message.reply_text(str(calendar.get_monthday_date(update.message.text)))
        if not context.chat_data['selected_date_start_for_compare']:
            context.chat_data['selected_date_start_for_compare'] = calendar.get_monthday_date(update.message.text)
            return names.SELECT_END_DATE_FOR_COMPARE
        else:
            context.chat_data['selected_date_start_for_compare'] = calendar.get_monthday_date(update.message.text)

        
      # return names.MAIN_MENU

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


select_start_date_for_compare_state = State(
    on_activate=activator,
    handlers=[
        MessageHandler(Filters.regex(f'({keyboards.BACK_BUTTON})'), back),
        MessageHandler(Filters.regex(f'({keyboards.CANCEL_BUTTON})'), back),
        MessageHandler(Filters.text, process_calendar),
    ]
)


