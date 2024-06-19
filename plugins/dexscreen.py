import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.dexscreener.com/latest/dex/tokens/{}"

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('Close', callback_data = 'close')]])

@Client.on_message(filters.text & filters.command)
async def reply_info(client, message):
    # Assuming tokens are unique enough, check if the message could be a token
    # This is a naive check; you might need more complex logic here
    if len(message.text.split()) == 1:
        query = message.text.strip()
        reply_markup = BUTTONS
        await message.reply_text(
            text=token_info(query),
            disable_web_page_preview=True,
            quote=True,
            reply_markup=reply_markup
        )

def token_info(token_id):
    try:
        r = requests.get(API.format(token_id))
        info = r.json()['pairs'][0]  # Adjusted to access the first item in 'pairs'
        base_token_name = info['baseToken']['name']
        base_token_symbol = info['baseToken']['symbol']
        price_usd = info['priceUsd']
        volume_24h = info['volume']['h24']
        price_change_24h = info['priceChange']['h24']
        liquidity_usd = info['liquidity']['usd']
        
        token_details = f"""--**Token Information**--
Name : `{base_token_name}`
Symbol : `{base_token_symbol}`
Price (USD) : `{price_usd}`
Volume (24h) : `{volume_24h}`
Price Change (24h) : `{price_change_24h}%`
Liquidity (USD) : `{liquidity_usd}`"""
        return token_details
    except Exception as error:
        return str(error)

# Example usage: /token GLMBN59oAM6bNAkhQcq1FNA9AvpUgjtKv2oAfQmQpump
