from typing import Optional, List

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.disable import DisableAbleCommandHandler

from telegraph import Telegraph, upload_file

@run_async
def media_telegraph(bot: Bot, update: Update):
    msg = update.effective_message # type: Optional[Message]


@run_async
def post_telegraph(bot: Bot, update: Update, args: List[str]):
    short_name = "Created By @MidukkiBot 😬"
    msg = update.effective_message # type: Optional[Message]
    telegraph = Telegraph()
    r = telegraph.create_account(short_name=short_name)
    auth_url = r["auth_url"]
    LOGGER.info(auth_url)
    title_of_page = " ".join(args)
    page_content = msg.reply_to_message.text
    page_content = page_content.replace("\n", "<br>")
    response = telegraph.create_page(
        title_of_page,
        html_content=page_content
    )
    msg.reply_text("https://telegra.ph/{}".format(response["path"]))


__help__ = """
○ My Name : Filter Bot
○ Creator : [D_ar_k_Angel](http://telegram.dog/D_ar_k_Angel)
○ Credits : `Everyone in this journey`
○ Language : Python3
○ Library : [Pyrogram asyncio 0.16.1](https://docs.pyrogram.org/)
○ Source Code : 👉 [Click Here](https://telegra.ph/file/c99524969744ed621f491.jpg)
○ Server : Heroku
○ Build Status : V4 `[+0.4]`
"""
__mod_name__ = "⚠️About⚠️"

