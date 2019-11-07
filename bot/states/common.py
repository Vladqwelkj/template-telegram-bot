from telegram import Update
from telegram.ext import CallbackContext

from extensions import StatesHandler


def back(update: Update, context: CallbackContext):
    return StatesHandler.BACK
