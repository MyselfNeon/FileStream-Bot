# ------------- Imports -------------
import sys
import os  # ✅ Added this — fixes the "os not defined" issue from config.py
import asyncio
import logging
import traceback
import logging.handlers as handlers
from FileStream.config import Telegram, Server, KEEP_ALIVE_URL  # 🟢 Includes KEEP_ALIVE_URL import
from aiohttp import web
from pyrogram import idle
import aiohttp  # 🟢 Needed for keep_alive()

from FileStream.bot import FileStream
from FileStream.server import web_server
from FileStream.bot.clients import initialize_clients

# ------------- Logging Setup -------------
logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
        handlers.RotatingFileHandler(
            "streambot.log",
            mode="a",
            maxBytes=104857600,
            backupCount=2,
            encoding="utf-8"
        )
    ],
)

logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# ------------- Server and Loop -------------
server = web.AppRunner(web_server())
loop = asyncio.get_event_loop()

# ------------- Keep Alive Function -------------
async def keep_alive():
    """Send a request every 300 seconds to keep the bot alive (if required)."""
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Sent keep-alive request.")
            except Exception as e:
                logging.error(f"Keep-alive request failed: {e}")
            await asyncio.sleep(300)

# ------------- Start Services -------------
async def start_services():
    print()
    if Telegram.SECONDARY:
        print("------------------ Starting as Secondary Server ------------------")
    else:
        print("------------------- Starting as Primary Server -------------------")
    print()
    print("-------------------- Initializing Telegram Bot --------------------")

    await FileStream.start()
    bot_info = await FileStream.get_me()
    FileStream.id = bot_info.id
    FileStream.username = bot_info.username
    FileStream.fname = bot_info.first_name
    print("------------------------------ DONE ------------------------------")
    print()
    print("---------------------- Initializing Clients ----------------------")
    await initialize_clients()
    print("------------------------------ DONE ------------------------------")
    print()
    print("--------------------- Initializing Web Server ---------------------")
    await server.setup()
    await web.TCPSite(server, Server.BIND_ADDRESS, Server.PORT).start()
    print("------------------------------ DONE ------------------------------")
    print()
    print("------------------------- Service Started -------------------------")
    print(f"                        bot =>> {bot_info.first_name}")
    if bot_info.dc_id:
        print(f"                        DC ID =>> {bot_info.dc_id}")
    print(f" URL =>> {Server.URL}")
    print("------------------------------------------------------------------")

    # 🟢 Start keep-alive loop in background
    if KEEP_ALIVE_URL:
        loop.create_task(keep_alive())

    await idle()

# ------------- Cleanup -------------
async def cleanup():
    await server.cleanup()
    await FileStream.stop()


# ------------- Main Entry Point -------------
if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        pass
    except Exception:
        logging.error(traceback.format_exc())
    finally:
        loop.run_until_complete(cleanup())
        loop.stop()
        print("------------------------ Stopped Services ------------------------")
        
