import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import Client, Filters 
from Tools.Download import download


@Client.on_message(Filters.command(["converttovideo"]))
async def video(c, m):
      await download(c, m)
      
