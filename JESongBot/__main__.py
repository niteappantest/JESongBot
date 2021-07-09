#    Copyright (C) 2021 - Infinity Bots
#    This programme is a part of JEBotZ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import bot
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Bot 🎵

Do /help for know about me!

A bot by **@WH173_5P1D3R**
"""

help_text = """
I can download HQ songs from YouTube Music

**Syntax** - `/song [song name]`

A bot by **@WH173_5P1D3R**
"""

@bot.on_message(filters.command("start") & ~filters.edited)
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="CONTACT OWNER", url="http://wh173-5p1d3r.rf.gd"
                    ),
                    InlineKeyboardButton(
                        text="CHANNEL", url="https://t.me/termux_tools_AA"
                    )
                ]
            ]
        )
        await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)
    else:
        start_text = "Hey [{}](tg://user?id={}), Song Bot is online ✅"
        await message.reply(start_text.format(name, user_id))
    
@bot.on_message(filters.command("help") & ~filters.edited)
async def start(client, message):
    await message.reply(help_text)

bot.start()
LOGGER.info("JESongBot is online.")
idle()
