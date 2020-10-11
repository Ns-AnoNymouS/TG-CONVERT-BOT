import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import pyrogram
import time
from pyrogram import Client, Filters 
from Tools.Download import download
from Tools.progress import progress_for_pyrogram

@Client.on_message(Filters.command(["converttovideo"]))
async def video(c, m):
      await download(c, m)
      logger.info("Downloading")
      await send.edit(Translation.UPLOAD_START)
      time = time.time()
      await c.send_video(
                chat_id=m.chat.id,
                video=media_location,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=True,
                thumb=thumb_image_path,
                reply_to_message_id=m.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    "Upload Status:",
                    send,
                    time
                )
      )
      try:
          os.remove(media_location)
      except:
          pass
      await send.edit_message_text(Translation.UPLOAD_COMPLETE)
