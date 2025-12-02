import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message
# --- Import database connection and owner ID from your config ---
from config import OWNER_ID
from database.db import db # Assuming your 'db' object is imported from 'database/db.py'
# ----------------------------------------------------------------

# Configure Admin List for filter
# OWNER_ID must be a list or a single integer. Assuming it's a single int for simplicity
ADMINS = [OWNER_ID]
# ---------------------------------------------------

@Client.on_message(filters.command("users") & filters.user(ADMINS))
async def users_count(bot: Client, message: Message):
    """
    Handles the /users command. Fetches total user count and exports all user 
    data (name, username, id) to a JSON file, then sends the file to the admin.
    """
    # 1. Initial status message
    msg = await message.reply_text("⏳ <b>__Gathering User Data...__</b>", quote=True)
    
    try:
        # Fetch total count
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
        
        # Iterate over users from the database cursor
        async for user in users_cursor:
            # Safely extract user details
            users_list.append({
                "name": user.get("name", "None"),
                "username": user.get("username", "None"),
                "id": user.get("id")
            })

        # Define temporary file path
        tmp_path = "user_database_export.json" 
        
        # Write data to JSON file
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(users_list, f, indent=2, ensure_ascii=False)

        # 3. Send the JSON file
        caption = f"📄 **Recorded {len(users_list)} Users**"
        await message.reply_document(
            document=tmp_path,
            caption=caption,
            quote=True
        )

        # 4. Cleanup
        try:
            os.remove(tmp_path)
        except Exception as e:
            print(f"[!] Failed to Delete File {tmp_path}: {e}")

    except Exception as e:
        # Handle errors during fetching or file creation
        await msg.edit_text(f"**__⚠️ Error Fetching User Data:__**\n<code>{e}</code>")
        print(f"[!] /users error: {e}")
