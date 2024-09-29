import os
import logging
from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION_STRING  # Ensure your config.py has these defined

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create the Telegram client
client = TelegramClient('user_bot', API_ID, API_HASH)

async def main():
    # Start the client using the session string
    await client.start(session=SESSION_STRING)

    logging.info("User bot started successfully.")

    # Load command plugins
    for filename in os.listdir("plugin"):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove the .py extension
            __import__(f"plugin.{module_name}")

    # Keep the bot running until disconnected
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
