import os
import logging
from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_STRING

# Set up logging
logging.basicConfig(level=logging.DEBUG)

client = TelegramClient('user_bot', API_ID, API_HASH)

async def main():
    await client.start(session=SESSION_STRING)
    logging.info("User bot started successfully.")

    for filename in os.listdir("plugin"):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            __import__(f"plugin.{module_name}")

    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
