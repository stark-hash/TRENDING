"""
Apache License 2.0
Copyright (c) 2022 @FDBotz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/FDBotz 
Repo Link : https://github.com
License Link : https://github.com
"""

import random
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command(["start","home"]))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention))       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("trending"))
async def trending(client, message):
    user = message.from_user
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.TRENDING_TXT.format(user.mention))       
    else:
        await message.reply_text(text=Txt.TRENDING_TXT.format(user.mention), disable_web_page_preview=True)


######################################################################################
##########################################################################################
BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("3 Hours | 3 SOL", callback_data="3_hours"),
        InlineKeyboardButton("6 Hours | 5.5 SOL", callback_data="6_hours")
    ],
    [
        InlineKeyboardButton("12 Hours | 9 SOL", callback_data="12_hours"),
        InlineKeyboardButton("24 Hours | 16 SOL", callback_data="24_hours")
    ]
])

@Client.on_message(filters.private & filters.text & filters.incoming)
async def reply_info_and_stringu(bot, message):
    user = message.from_user
    user_id = message.from_user.id

    # Ignore commands and hashtags
    if message.text.startswith("/") or message.text.startswith("#"):
        return

    # Check if message contains exactly 15 or 20 characters
    if len(message.text) == 15 or len(message.text) == 20:
        await message.reply_text(
            "Finder Trending Boost 💎\n\n"
            "Boost your token visibility and amplify its volume\n\n"
            "Enjoy a limited-time 25% off sale!\n\n"
            "➤ Select the trending time below",
            reply_markup=BUTTONS
        )
        return

    # Check if message contains fewer than 15 characters
    if len(message.text) < 15:
        await message.reply_text(
            "Reply to this message with the CA of the token you would like to purchase Finder Trending for.",
            reply_markup=BUTTONS
        )
        return
############################################################################################


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
        )

     
    elif data == "refer_friends":
        await query.send_message(
            text=Txt.REFER_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )
    elif data == "3_hours":
        await query.message.edit_text(
            text=Txt.THREEHRS_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Paid", callback_data="paid")
            ]])
        )
    elif data == "6_hours":
        await query.send_message(
            text=Txt.SIXHRS_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Paid", callback_data="paid")
            ]])
        )
    elif data == "12_hours":
        await query.send_message(
            text=Txt.TWELVEHRS_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Paid", callback_data="paid")
            ]])
        )
    elif data == "24_hours":
        await query.send_message(
            text=Txt.TWOFOURHRS_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Paid", callback_data="paid")
            ]])
        )


    elif data == "paid":
        await query.send_message(
            text=Txt.PAYMENT_TXT,
            disable_web_page_preview=True,
        )


    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()




