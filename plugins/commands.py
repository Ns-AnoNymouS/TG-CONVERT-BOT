import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from config import Config 
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation
from Tools.Download import download



my_father = "https://t.me/{}".format(Config.USER_NAME[1:])
support = "https://telegram.dog/Ns_Bot_supporters"

@Client.on_message(Filters.command(["start"]))
async def start(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.START.format(m.from_user.first_name, Config.USER_NAME),
                         reply_to_message_id=m.message_id,
                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("My Father 👨‍💻", url=my_father), InlineKeyboardButton("📌Support channel", url=support)]]))
    logger.info(f"{m.from_user.first_name} used start command")



@Client.on_message(Filters.command(["help"]))
async def help(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")


@Client.on_message(Filters.command(["about"]))
async def about(c, m):

    await c.send_message(chat_id=m.chat.id,
                         text=Translation.ABOUT,
                         disable_web_page_preview=True,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")

@Client.on_message(Filters.command(["converttovideo"]))
async def video(c, m):

  if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
      return
  if m.from_user.id not in Config.BANNED_USER:
      if m.reply_to_message is not None:
          await download(c, m)
      else:
          await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(Filters.command(["converttofile"]))
async def file(c, m):

  if Config.BOT_PWD:
      if (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
          await m.reply_text(text=Translation.NOT_LOGGED_TEXT, quote=True)
          return
      else:
          pass
  if m.from_user.id in Config.BANNED_USER:
      await c.send_message(chat_id=m.chat.id, text=Translation.BANNED_TEXT)
  if m.from_user.id not in Config.BANNED_USER:
    if m.reply_to_message is not None:
      await download(c, m)
    else:
       await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(Filters.command(["login"]))
async def login(c, m):
    if Config.BOT_PWD:
        if (len(m.command) >= 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            _, password = m.text.split(" ", 1)
            if str(password) == str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.SUCESS_LOGIN,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")
                return Config.LOGGED_USER.append(m.from_user.id)
            if str(password) != str(Config.BOT_PWD):
                await c.send_message(chat_id=m.chat.id,
                                     text=Translation.WRONG_PWD,
                                     disable_web_page_preview=True,
                                     reply_to_message_id=m.message_id,
                                     parse_mode="markdown")

        if (len(m.command) < 2) & (m.from_user.id not in Config.LOGGED_USER) & (m.from_user.id not in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text="Use this command for login to this bot. Semd the passwordin the format 👉`/login Bot password`.",
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")

        if (m.from_user.id in Config.LOGGED_USER)|(m.from_user.id in Config.AUTH_USERS):
            await c.send_message(chat_id=m.chat.id,
                                 text=Translation.EXISTING_USER,
                                 disable_web_page_preview=True,
                                 reply_to_message_id=m.message_id,
                                 parse_mode="markdown")
