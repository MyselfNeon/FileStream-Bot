# ------- imports -------
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

# ------- language text -------
class LANG(object):

    START_TEXT = """
<b><i><blockquote>👋 Yoo !! {}</blockquote></i></b>
<b><i><blockquote>I’ᴍ A Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇ Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ.\nPʀᴏᴠɪᴅɪɴɢ Iɴsᴛᴀɴᴛ Sᴛʀᴇᴀᴍɪɴɢ Aɴᴅ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋs 🖇️</i></b>\n
<b><i>Fᴜʟʟʏ Oᴘᴛɪᴍɪᴢᴇᴅ Fᴏʀ Bᴏᴛʜ Cʜᴀɴɴᴇʟs Aɴᴅ Pʀɪᴠᴀᴛᴇ Cʜᴀᴛs 🧩</i></b>\n
<b><i>💕 @{}</i></b></blockquote>"""

    HELP_TEXT = """
<b><i>➠ Aᴅᴅ Mᴇ As Aɴ Aᴅᴍɪɴ Iɴ Cʜᴀɴɴᴇʟ</i></b>
<b><i>➠ Sᴇɴᴅ Mᴇ Aɴʏ Dᴏᴄᴜᴍᴇɴᴛ Oʀ Mᴇᴅɪᴀ</i></b>
<b><i>➠ I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Sᴛʀᴇᴀᴍᴀʙʟᴇ Lɪɴᴋ</i></b>\n
<b><i>Aᴅᴜʟᴛ Cᴏɴᴛᴇɴᴛ Sᴛʀɪᴄᴛʟʏ Pʀᴏʜɪʙɪᴛᴇᴅ.</i></b>\n
<i><b>🧑‍💻 Rᴇᴘᴏʀᴛ Bᴜɢs Tᴏ <a href='https://telegram.me/myselfneon'>Dᴇᴠᴇʟᴏᴘᴇʀ 👮</a></b></i>"""

    ABOUT_TEXT = """
<b><i>➠ Mʏ Nᴀᴍᴇ : {}</i></b>\n
<b><i>➠ Vᴇʀsɪᴏɴ : {} [Stable]</i></b>
<b><i>➠ Uᴘᴅᴀᴛᴇᴅ Oɴ : 28 September 2025</i></b>
<b><i>➠ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/MyselfNeon'>MyselfNeon</a></i></b> 
<b><i>➠ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a></i></b> 
<b><i>➠ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 𝟹</a></i></b> 
<b><i>➠ DᴀᴛᴀBᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ DB</a></i></b> 
<b><i>➠ Bᴏᴛ Sᴇʀᴠᴇʀ : <a href='https://heroku.com'>Hᴇʀᴏᴋᴜ</a></i></b> 
"""

    STREAM_TEXT = """
<u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u>\n
<b>📂 Fɪʟᴇ Nᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ Sɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b>\n<code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b>\n<code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b>\n<code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ Nᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ Sɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b>\n<code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b>\n<code>{}</code>\n"""

    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Mᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


# ------- inline buttons -------
class BUTTON(object):

    START_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Hᴇʟᴘ 🆘', callback_data='help'),
                InlineKeyboardButton('Aʙᴏᴜᴛ 😎', callback_data='about')
            ],
            [
                InlineKeyboardButton("🔥 Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')
            ]
        ]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴘ 🦠', url='https://t.me/+o1s-8MppL2syYTI9'),
                InlineKeyboardButton("Aʙᴏᴜᴛ 😎", callback_data='about')
            ],
            [
                InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data='close'),
                InlineKeyboardButton('Hᴏᴍᴇ 🏠', callback_data='home')
            ]
        ]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Hᴇʟᴘ 🆘', callback_data='help'),
                InlineKeyboardButton('Sᴏᴜʀᴄᴇ 🚀', url='https://github.com/MyselfNeon')
            ],
            [
                InlineKeyboardButton('Cʟᴏsᴇ ❌', callback_data='close'),
                InlineKeyboardButton('Bᴀᴄᴋ ⬅️', callback_data='home')
            ]
        ]
    )
