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
            text = f"<b>🧑‍💻 Developer : <a href='tg://user?id={OWNER_ID}'>꧁𓊈𒆜ᴍᴜᴢᴀғғᴀʀ𒆜𓊉꧂</a>\n📝 Language : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>\n📚 Library : <a href='https://docs.pyrogram.org/'>Pyrogram</a>\n🚀 Server : <a href='https://heroku.com/'>Heroku</a>\n📢 Channel : <a href='https://t.me/Mrn_Officialx'>Mrn_Officialx</a>\n🤖 My Name : <a href='https://t.me/Files_SharingXbot'>File Sharing Bot</a></b>",
            disable_web_page_preview = True,,
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
