import pyrogram 
from translation import Translation
import time
from Tools.progress import progress_for_pyrogram
#Download the media

async def download(c, m):
   send = await c.send_message(chat_id=m.chat.id,
                          text=Translation.DOWNLOAD_START,
                          reply_to_message_id=m.message_id)


   download_location = Config.DOWNLOAD_LOCATION + "/" + m.from_user.id                                                                 
   time = time.time()
   media_location = await c.download_media(
                          message=m.reply_to_message,
                          file_name=download_location,
                          progress=progress_for_pyrogram,
                          progress_args=(
                               "Download Status:",
                               send,
                               time
                          )
                    )
   if not media_location is None:
      await send.edit(Translation.DOWNLOAD_COMPLETE)
