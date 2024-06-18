import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.dexscreener.com/latest/dex/tokens/"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('Close', callback_data="close")]])

@Client.on_message(filters.command("token"))
async def reply_info(client, message):
    try:
        query = message.text.split(None, 1)[1]
        reply_markup = BUTTONS
        await message.reply_text(
            text=token_info(query),
            disable_web_page_preview=True,
            quote=True,
            reply_markup=reply_markup
        )
    except IndexError:
        await message.reply_text(
            text="Please provide a token.",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=reply_markup
        )

def token_info(token_address):
    try:
        r = requests.get(API + requote_uri(token_address))
        info = r.json()

        # Extracting information from the response
        name = info.get('name')
        symbol = info.get('symbol')
        price = info.get('priceUsd')


        token_info = f"""--**Token Information**--
Name : `{name}`
Symbol : `{symbol}`
Price (USD) : `{price}`"""
        
        return token_info
    except Exception as error:
        return f"An error occurred: {error}"