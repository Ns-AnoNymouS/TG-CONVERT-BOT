import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    USER_NAME = os.environ.get("USER_NAME", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    BOT_PWD = os.environ.get("BOT_PASSWORD", "")
    LOGGED_USER = []
    DB_URI = os.environ.get("DATABASE_URL", "")
