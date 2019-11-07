from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from bot.resources import messages
from bot.states import names


from bot.states.main.menu import main_menu_state
from bot.states.organisator.menu import organisator_menu_state
from bot.states.hello_habit.menu import hello_habit_menu_state

from bot.states.analytics.menu import analytics_menu_state
from bot.states.analytics.custom_period.select_start_date import select_start_date_state
from bot.states.analytics.custom_period.select_end_date import select_end_date_state
from bot.states.analytics.custom_period.select_start_date_for_compare import select_start_date_for_compare_state
from bot.states.analytics.custom_period.select_end_date_for_compare import select_end_date_for_compare_state

from bot.states.reviews.menu import reviews_menu_state
from bot.states.reviews.new_reviews import new_reviews_state
from bot.states.reviews.review_reply import review_reply_state

from bot.states.message.message_write import messsage_write_state
from bot.states.message.send_log import message_log_state
from bot.states.message.message_send import message_send_state

from bot.states.contacts.contacts import contacts_state

from bot.states.organisator.moderation.menu import moderation_menu_state
from bot.states.organisator.marathons.marathons import marathons_menu_state


from extensions import StatesHandler
from services import user


def entry(update: Update, context: CallbackContext):
    user.create_from_update(update)

    update.message.reply_text(messages.HELLO_MESSAGE)

    return names.MAIN_MENU


states_handler = StatesHandler(
    entry_point=CommandHandler('start', entry),
    states={
        names.MAIN_MENU: main_menu_state,
        names.ORGANISATOR_MENU: organisator_menu_state,###
        names.HELLO_HABIT_MENU: hello_habit_menu_state,

        # Common states:
        names.ANALYTICS_MENU: analytics_menu_state,
        names.SELECT_START_DATE: select_start_date_state,
        names.SELECT_END_DATE: select_end_date_state,
        names.SELECT_START_DATE_FOR_COMPARE: select_start_date_for_compare_state,
        names.SELECT_END_DATE_FOR_COMPARE: select_end_date_for_compare_state,

        names.REVIEWS_MENU: reviews_menu_state,
        names.REVIEWS_NEW: new_reviews_state,
        names.REVIEW_REPLY: review_reply_state,

        names.MESSSAGE_WRITE: messsage_write_state,
        names.MESSAGE_LOG: message_log_state,
        names.MESSAGE_SEND: message_send_state,

        names.CONTACTS_MENU: contacts_state,
        
        # Only in 'organisator' way:
        names.MARATHONS_MENU: marathons_menu_state,
        names.MODERATION_MENU: moderation_menu_state,



    
    }
)
