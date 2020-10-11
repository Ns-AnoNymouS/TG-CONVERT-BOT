import pyrogram 
from translation import Translation

#Download the media

async def download(c, m, media):
   await c.send_message(chat_id=m.chat.id,
                          text=Translation.DOWNLOAD_START,
                          reply_to_message_id=..message_id)
   await c.download_media(
