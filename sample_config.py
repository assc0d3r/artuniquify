#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
from decouple import config

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
AUTH_USERS = config(" AUTH_USERS")
TG_USER_SESSION = config("TG_USER_SESSION")
TG_BOT_TOKEN = config(" TG_BOT_TOKEN")



logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
