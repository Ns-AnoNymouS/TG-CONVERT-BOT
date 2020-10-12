import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from config import Config 
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation
from Tools.Download import download

my_father = "tg://user?id={}".format(Config.USER_ID)
support = "https://telegram.dog/Ns_Bot_supporters"
@Client.on_message(Filters.command(["start"]))
async def start(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.START.format(m.from_user.first_name, Config.OWNER_NAME),
                         reply_to_message_id=m.message_id,
                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("My Father 👨‍💻", url=my_father), InlineKeyboardButton("📌Support channel", url=support)]]))
    logger.info(f"{m.from_user.first_name} used start command")



@Client.on_message(Filters.command(["help"]))
async def help(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message_id=m.message_id),
                         parse_mode="markdown")


@Client.on_message(Filters.command(["about"]))
async def about(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.ABOUT,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")

@Client.on_message(Filters.command(["converttovideo"]))
async def video(c, m):
      await download(c, m)

@Client.on_message(Filters.command(["converttofile"]))
async def file(c, m):
      await download(c, m)
