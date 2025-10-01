#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><blockquote>⍟───[ ᴍʏ ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote> \n‣ 🎭 Mʏ Nᴀᴍᴇ:  <a href=https://t.me/{}>{}</a>\n‣ 💞 ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> \n‣ 🇮🇳 Cʀᴇᴀᴛᴏʀ : <a href={}>꧁𓊈𒆜𝖒𝖎𝖒𝖆𝖒_𝖔𝖋𝖋𝖎𝖈𝖎𝖆𝖑𒆜𓊉꧂</a> \n‣ ⚙️ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> \n‣ 🍿 Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>\n‣ 🐍 DᴀᴛᴀBᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> \n‣ ⚙️ Bᴏᴛ Sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> \n‣ ⚙️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
