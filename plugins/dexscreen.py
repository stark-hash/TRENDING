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
        name = info.get('name', 'N/A')
        symbol = info.get('symbol', 'N/A')
        price = info.get('price', {}).get('usd', 'N/A')
        market_cap = info.get('marketCap', 'N/A')
        volume_24h = info.get('volume', {}).get('usd', 'N/A')
        price_change_24h = info.get('priceChange', {}).get('percentage', {}).get('24h', 'N/A')

        token_info = f"""--**Token Information**--
Name : `{name}`
Symbol : `{symbol}`
Price (USD) : `{price}`
Market Cap : `{market_cap}`
24h Volume (USD) : `{volume_24h}`
24h Price Change (%) : `{price_change_24h}`"""
        
        return token_info
    except Exception as error:
        return f"An error occurred: {error}"
    
