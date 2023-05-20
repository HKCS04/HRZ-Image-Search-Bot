import sys
import time
from uuid import uuid4

from telebot import TeleBot, types

import texts
from api.cse import CSEAPIError, GoogleSearchEngine, SearchResult
from ext import parse_query
from loggers import logger

TG_API_TOKEN = os.environ["TG_API_TOKEN"]
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
SEARCH_ENGINE_ID = os.environ["SEARCH_ENGINE_ID"]

if not all((TG_API_TOKEN, GOOGLE_API_KEY, SEARCH_ENGINE_ID)):
    logger.error("Missing environment variables! Exiting...")
    sys.exit(1)

bot = TeleBot("6197005764:AAEDM3U2kt96GyiTVmDl4nOsnXlJX3QADNc", parse_mode="Markdown")
cse = GoogleSearchEngine(GOOGLE_API_KEY, SEARCH_ENGINE_ID)

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

force_channel = "TheHRZTG"

PICS = [
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
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
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
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
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
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheHRZTG"),
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

@Bot.inline_handler(func=lambda query: len(query.query) > 6)
def inline_query_handler(inline_query: types.InlineQuery) -> None:
    """Handle every inline query that is not empty."""
    parsed_query = parse_query(inline_query.query)
    # query string without commands
    query_text = parsed_query.query
    query_id = str(inline_query.id)
    results = []
    not_found = types.InlineQueryResultArticle(
        id=str(uuid4()),
        title="⚠️ No results found",
        description=texts.NOT_FOUND_MSG,
        input_message_content=types.InputTextMessageContent(
            message_text="not_found_result"
        )
    )
    page = 1
    # handle query commands
    if parsed_query.commands:
        for command in parsed_query.commands:
            if command.name.lower() == "":
                try:
                    value = abs(int(command.value))
                    page = value if value > 1 else 1
                except ValueError:
                    continue
    try:
        search_result: SearchResult = cse.search(
            query=query_text,
            page=page,
            only_image=True
        )
    except CSEAPIError as e:
        logger.error(f"Error while searching for {query_text!r}: {e}")
        bot.answer_inline_query(query_id, [])
    else:
        # for every item in search result that has image attribute, add it to results
        if search_result.items:
            for item in search_result.items:
                if item.image:
                    results.append(
                        types.InlineQueryResultPhoto(
                            id=str(uuid4()),
                            photo_url=item.link,
                            thumb_url=item.image.thumbnailLink,
                            photo_width=item.image.width,
                            photo_height=item.image.height,
                            title=item.title
                        )
                    )
        if search_result.spelling:
            results.append(
                types.InlineQueryResultArticle(
                    id=str(uuid4()),
                    title="✍🏻 Spelling suggestion",
                    description=texts.SPELLING_MSG.format(
                        corrected_query=search_result.spelling["correctedQuery"]
                    ),
                    input_message_content=types.InputTextMessageContent(
                        message_text="spelling_suggestion"
                    )
                )
            )
    if not results:
        Bot.answer_inline_query(query_id, [not_found])
    else:
        Bot.answer_inline_query(query_id, results, cache_time=60)


# message handler
@Bot.message_handler(func=lambda message: True)
def message_handler(message: types.Message) -> None:
    """Handle every message that is not a command."""
    text = message.text
    chat_id = message.chat.id
    message_id = message.message_id

    if text in ("not_found_result", "spelling_suggestion"):
        bot.delete_message(chat_id, message_id)
        return

    kb = [
        [
            types.InlineKeyboardButton(
                "Search 🔎",
                switch_inline_query_current_chat=text
            )
        ]
    ]

    Bot.send_message(
        chat_id,
        texts.PRIVATE_SEARCH_MSG.format(query=text),
        reply_to_message_id=message_id,
        reply_markup=types.InlineKeyboardMarkup(kb)
    )


def start_polling() -> None:
    """Start polling and responding to every message."""
    logger.info("Bot polling started...")
    Bot.infinity_polling()
    while True:
        time.sleep(2)


if __name__ == '__main__':
    try:
        start_polling()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
        cse.close()
        sys.exit()


Bot.run()
