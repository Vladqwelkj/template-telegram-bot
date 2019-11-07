import logging

from telegram.ext import Updater

from bot.states.handler import states_handler
from config import Config
from db import init_db

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

REQUEST_KWARGS={
    'proxy_url': Config.PROXY_URL,
    # Optional, if you need authentication:
   # 'username': 'PROXY_USER',
  #  'password': 'PROXY_PASS',
}

def error_handler(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    init_db()

    updater = Updater(Config.BOT_TOKEN, request_kwargs=REQUEST_KWARGS, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(states_handler)
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
