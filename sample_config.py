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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5897885316:AAEchiE7Kpm_EObAW_6PHaTXWZuTiiGQW88")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "10038985"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b13a9434d5f59fdb592bf3cd0f457eff")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "-1001187675214").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "1BJWap1sBu39Ddw2DOQaifrJGIdQucKkAZCuv4WorKu9vnmMJCK8dhbY_MDmlHPlgBxyKtL_kejFqD0nEGCrbvxUXaxjTQl__UICAU3mCYxawTbG3AL4r0kU_lxCxxVrsY33GN0kknH3yQe-WWdbip8pH0w5knoo0x2Ik9B3x9v8O7wMP3VxveWlUVf1BLs3KXenvg5QQL1DEAGsFlSbCOwOBz2Dw4mfiRLBIavrCYFRylxFQWlkuGwLa1dyHEl37Se46alMp3Cb72FahHQ8u8BpEyziqKIsrNLcZij7NvSKa2j97My0q5xl4pZi-P50XBf9xGfs1VqppBEEytrHKt-gtYO4XTXA=")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
