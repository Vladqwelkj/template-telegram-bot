import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    PROXY_URL = os.environ.get('PROXY_URL')
    DB_URL = os.environ.get('DB_URL')
