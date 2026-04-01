#!/usr/bin/python
import asyncio
import logging
import os
from decouple import config
from telethon import TelegramClient, events

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

api_id = config('API_ID')
api_hash = config('API_HASH')
reciever = int(config('RECIEVER'))

client = TelegramClient(
    'default',
    api_id,
    api_hash,
)

os.makedirs('media/', exist_ok=True)

@client.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video and (not e.video_note)) and e.media_unread))
async def downloader(event):
    result = await event.download_media(file='media/')
    await client.send_file(reciever, result)

async def main():
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
