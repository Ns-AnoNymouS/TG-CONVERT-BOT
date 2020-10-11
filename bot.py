import pyrogram

from pyrogram import Client 

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "CONVERTBOT",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    Config.AUTH_USERS.add(1337144652)
    app.run()
