# ---------------------------------------------------
# File Name: Stream.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22 (Merged with /users command)
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import asyncio
import json
import os
from FileStream.bot import FileStream, multi_clients
from FileStream.utils.bot_utils import (
    is_user_banned,
    is_user_exist,
    is_user_joined,
    gen_link,
    is_channel_banned,
    is_channel_exist,
    is_user_authorized
)
from FileStream.utils.database import Database
from FileStream.utils.file_properties import get_file_ids, get_file_info
from FileStream.config import Telegram
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

ADMINS = [Telegram.OWNER_ID]

@FileStream.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.video_note
        | filters.audio
        | filters.voice
        | filters.animation
        | filters.photo
    ),
    group=4,
)
async def private_receive_handler(bot: Client, message: Message):
    if not await is_user_authorized(message):
        return
    if await is_user_banned(message):
        return

    await is_user_exist(bot, message)
    if Telegram.FORCE_SUB:
        if not await is_user_joined(bot, message):
            return

    try:
        inserted_id = await db.add_file(get_file_info(message))
        await get_file_ids(False, inserted_id, multi_clients, message)
        reply_markup, stream_text = await gen_link(_id=inserted_id)
        await message.reply_text(
            text=stream_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )

    except FloodWait as e:
        print(f"Sleeping for {str(e.value)}s")
        await asyncio.sleep(e.value)
        await bot.send_message(
            chat_id=Telegram.ULOG_CHANNEL,
            text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.value)}s ғʀᴏᴍ [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\n**ᴜsᴇʀ ɪᴅ :** `{str(message.from_user.id)}`",
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN
        )

@FileStream.on_message(
    filters.channel
    & ~filters.forwarded
    & ~filters.media_group
    & (
        filters.document
        | filters.video
        | filters.video_note
        | filters.audio
        | filters.voice
        | filters.photo
    )
)
async def channel_receive_handler(bot: Client, message: Message):
    # Ignore messages from ULOG and FLOG Channels
    if int(message.chat.id) in [Telegram.ULOG_CHANNEL, Telegram.FLOG_CHANNEL]:
        return

    if await is_channel_banned(bot, message):
        return

    await is_channel_exist(bot, message)

    try:
        inserted_id = await db.add_file(get_file_info(message))
        await get_file_ids(False, inserted_id, multi_clients, message)
        reply_markup, stream_link = await gen_link(_id=inserted_id)
        await bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ 📥",
                                       url=f"https://t.me/{FileStream.username}?start=stream_{str(inserted_id)}")]]
            )
        )

    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(
            chat_id=Telegram.ULOG_CHANNEL,
            text=f"ɢᴏᴛ ғʟᴏᴏᴅᴡᴀɪᴛ ᴏғ {str(w.x)}s ғʀᴏᴍ {message.chat.title}\n\n**ᴄʜᴀɴɴᴇʟ ɪᴅ :** `{str(message.chat.id)}`",
            disable_web_page_preview=True
        )

    except Exception as e:
        await bot.send_message(
            chat_id=Telegram.ULOG_CHANNEL,
            text=f"**#EʀʀᴏʀTʀᴀᴄᴋᴇʙᴀᴄᴋ:** `{e}`",
            disable_web_page_preview=True
        )
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Gɪᴠᴇ ᴍᴇ ᴇᴅɪᴛ ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ʙɪɴ Cʜᴀɴɴᴇʟ!{e}**")

@FileStream.on_message(filters.command("users") & filters.user(ADMINS))
async def users_count(bot: Client, message: Message):
    """
    Handles the /users command. Provides user statistics and exports the entire 
    user list (name, username, id) as a JSON file to the admin.
    """
    msg = await message.reply_text("⏳ <b>__Gathering User Data...__</b>", quote=True)
    try:
        # 1. Fetch total count
        total = await db.total_users_count()
        
        # Update status with count
        await msg.edit_text(
            f"""
🌀 <b><i>User Analytics Update</i></b> 🌀

👥 <b>Total Registered Users:</b> {total}
🛰 <b>System Status:</b> Active ✅
🧠 <b>Data Source:</b> MongoDB (async)
"""
        )

        # 2. Prepare and export user data to JSON
        users_cursor = await db.get_all_users()
        users_list = []
        async for user in users_cursor:
            # Collect user data from the database cursor
            users_list.append({
                "name": user.get("name", "None"),
                "username": user.get("username", "None"),
                "id": user.get("id")
            })

        # Define temporary filename - NOW SET TO FileStreamBot.json
        tmp_path = "FileStreamBot.json" 
        
        # Write data to JSON file
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(users_list, f, indent=2, ensure_ascii=False)

        # 3. Send the JSON file
        caption = f"📄 **Recorded {len(users_list)} Users**"
        await message.reply_document(
            document=tmp_path,
            caption=caption
        )

        # 4. Cleanup
        try:
            os.remove(tmp_path)
        except Exception as e:
            print(f"[!] Failed to Delete File {tmp_path}: {e}")

    except Exception as e:
        await msg.edit_text(f"**__⚠️ Error Fetching User Data:__**\n<code>{e}</code>")
        print(f"[!] /users error: {e}")


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
