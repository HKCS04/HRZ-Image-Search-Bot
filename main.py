import os
import requests
from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto
from pyrogram.types import CallbackQuery
import random
from pyrogram.errors import UserNotParticipant


Bot = Client(
    "Image-Search-Bot",
    bot_token="6197005764:AAEDM3U2kt96GyiTVmDl4nOsnXlJX3QADNc",
    api_id="23050566",
    api_hash="25e954ccd4afb778eea69bd6754275ff"
)

API = "https://apibu.herokuapp.com/api/y-images?query="

force_channel = "TheHRZTG""

PIC = [
 "https://telegra.ph/file/92440733ad3c34c211531.jpg"
]

START_TEXT = """ʜᴇʟʟᴏ {},

ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ᴅᴇᴀʀ 🙌🏻
ɪᴛ ɪꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴊᴜꜱᴛ ᴇɴᴛᴇʀ ᴍʏ ᴜꜱᴇʀɴᴀᴍᴇ ᴀɴᴅ ɪᴍᴀɢᴇ ɴᴀᴍᴇ 🎊
ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴀᴛᴀɪʟꜱ ʜɪᴛ /help...

@TheHRZTG"""

HELP_TEXT = """This bot can help you find and share images. It works automatically, no need to add it anywhere. 
Simply open any of your chats and type @HRZPicRobot something in the message field. Then tap on a result to send.

For example, try typing @HRZPicRobot funny cat here."""

ABOUT_TEXT = """➥ Name : [HRZ Image Search Bot](http://t.me/HRZPicRobot)
    
➥ Creator : [HRZ🇮🇳](https://t.me/HRZRobot)

➥ Language : Python3

➥ Library : [Pyrogram V2](https://docs.pyrogram.org/)

➥ Source Code : [Click Here](t.me/TheHRZTG)"""

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="🔊 Join Our Main Channel to Use Me",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 😁", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_TEXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
            ],[
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/HRZRobot"),
            ],[
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="t.me/HRZSupport")
            ]]
            )
        )

@Bot.on_message(filters.private & filters.command(["help"]))
async def help(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_TEXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
            ],[
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/HRZRobot"),
            ],[
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="t.me/HRZSupport")
            ]]
            )
        )
        
@Bot.on_message(filters.private & filters.command(["about"]))
async def about(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ABOUT_TEXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
            ],[
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/HRZRobot"),
            ],[
            InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="t.me/HRZSupport")
            ]]
            )
        )
        
@Bot.on_message(filters.private & filters.text)
async def filter_text(bot, update):
    
    await update.reply_text(
        text=f"Click the button below for searching your query.\n\nQuery: `{update.text}`",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Search Here", switch_inline_query_current_chat=update.text)],
                [InlineKeyboardButton(text="Search in another chat", switch_inline_query=update.text)]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_inline_query()
async def search(bot, update):
    
    results = requests.get(
        API + requests.utils.requote_uri(update.query)
    ).json()["result"][:50]
    
    answers = []
    for result in results:
        answers.append(
            InlineQueryResultPhoto(
                title=update.query.capitalize(),
                description=result,
                caption="@TheHRZTG",
                photo_url=result
            )
        )
    
    await update.answer(answers)


Bot.run()
