# ------------- Imports -------------
import os
import time
import string
import random
import asyncio
import aiofiles
import datetime

from FileStream.utils.broadcast_helper import send_msg
from FileStream.utils.database import Database
from FileStream.bot import FileStream
from FileStream.server.exceptions import FIleNotFound
from FileStream.config import Telegram, Server
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums.parse_mode import ParseMode

# ------------- Database Setup -------------
db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)
broadcast_ids = {}

# ------------- /status Command -------------
@FileStream.on_message(filters.command("status") & filters.private & filters.user(Telegram.OWNER_ID))
async def sts(c: Client, m: Message):
    await m.reply_text(
        text=f"""**📊 Bot Status**
**Total Users:** `{await db.total_users_count()}`
**Banned Users:** `{await db.total_banned_users_count()}`
**Total Links Generated:** `{await db.total_files()}`""",
        parse_mode=ParseMode.MARKDOWN,
        quote=True
    )

# ------------- /ban Command -------------
@FileStream.on_message(filters.command("ban") & filters.private & filters.user(Telegram.OWNER_ID))
async def ban_user(b, m: Message):
    if len(m.command) < 2:
        return await m.reply_text(
            "**⚠️ Usage:** `/ban <user_id>`\nExample: `/ban 123456789`",
            parse_mode=ParseMode.MARKDOWN,
            quote=True
        )

    id = m.text.split("/ban ")[-1]
    if not await db.is_user_banned(int(id)):
        try:
            await db.ban_user(int(id))
            await db.delete_user(int(id))
            await m.reply_text(f"`{id}` **has been banned.**", parse_mode=ParseMode.MARKDOWN, quote=True)
            if not str(id).startswith('-100'):
                await b.send_message(
                    chat_id=id,
                    text="**🚫 You have been banned from using the bot.**",
                    parse_mode=ParseMode.MARKDOWN
                )
        except Exception as e:
            await m.reply_text(f"**Something went wrong:** `{e}`", parse_mode=ParseMode.MARKDOWN, quote=True)
    else:
        await m.reply_text(f"`{id}` **is already banned.**", parse_mode=ParseMode.MARKDOWN, quote=True)

# ------------- /unban Command -------------
@FileStream.on_message(filters.command("unban") & filters.private & filters.user(Telegram.OWNER_ID))
async def unban_user(b, m: Message):
    if len(m.command) < 2:
        return await m.reply_text(
            "**⚠️ Usage:** `/unban <user_id>`\nExample: `/unban 123456789`",
            parse_mode=ParseMode.MARKDOWN,
            quote=True
        )

    id = m.text.split("/unban ")[-1]
    if await db.is_user_banned(int(id)):
        try:
            await db.unban_user(int(id))
            await m.reply_text(f"`{id}` **has been unbanned.**", parse_mode=ParseMode.MARKDOWN, quote=True)
            if not str(id).startswith('-100'):
                await b.send_message(
                    chat_id=id,
                    text="**✅ You have been unbanned! You can now use the bot again.**",
                    parse_mode=ParseMode.MARKDOWN
                )
        except Exception as e:
            await m.reply_text(f"**Something went wrong:** `{e}`", parse_mode=ParseMode.MARKDOWN, quote=True)
    else:
        await m.reply_text(f"`{id}` **is not banned.**", parse_mode=ParseMode.MARKDOWN, quote=True)

# ------------- /broadcast Command -------------
@FileStream.on_message(filters.command("broadcast") & filters.private & filters.user(Telegram.OWNER_ID))
async def broadcast_(c, m):
    # Check if the command is used as a reply
    if not m.reply_to_message:
        return await m.reply_text(
            "**⚠️ Usage:** Reply to a message with `/broadcast`\nExample: reply to a text or media → `/broadcast`",
            parse_mode=ParseMode.MARKDOWN,
            quote=True
        )

    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text("📢 **Broadcast started!**\nYou’ll get the log when it’s done.")

    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)

    async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user['id']), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current=done, failed=failed, success=success))
                try:
                    await out.edit_text(f"📊 **Broadcast Progress**\n\n✅ Success: {success}\n❌ Failed: {failed}\n📦 Processed: {done}/{total_users}")
                except:
                    pass

    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"✅ **Broadcast completed in** `{completed_in}`\n\nTotal users: {total_users}\nSuccess: {success}\nFailed: {failed}",
            quote=True
        )
    else:
        await m.reply_document(
            document='broadcast.txt',
            caption=f"✅ **Broadcast completed in** `{completed_in}`\n\nTotal users: {total_users}\nSuccess: {success}\nFailed: {failed}",
            quote=True
        )
    os.remove('broadcast.txt')

# ------------- /del Command -------------
@FileStream.on_message(filters.command("del") & filters.private & filters.user(Telegram.OWNER_ID))
async def del_file(c: Client, m: Message):
    file_id = m.text.split(" ")[-1]
    if len(m.command) < 2:
        return await m.reply_text(
            "**⚠️ Usage:** `/del <file_id>`\nExample: `/del abc123xyz`",
            parse_mode=ParseMode.MARKDOWN,
            quote=True
        )
    try:
        file_info = await db.get_file(file_id)
    except FIleNotFound:
        return await m.reply_text("**🗑 File already deleted.**", quote=True)
    await db.delete_one_file(file_info['_id'])
    await db.count_links(file_info['user_id'], "-")
    await m.reply_text("✅ **File deleted successfully!**", quote=True)
