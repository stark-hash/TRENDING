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
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("Buy", callback_data='buy'),
        InlineKeyboardButton("Sell & Manage", callback_data='sell_manage')
        ],[
        InlineKeyboardButton("Help", callback_data='help'),
        InlineKeyboardButton("Refer Friends", callback_data='refer_friends'),
        InlineKeyboardButton("Alerts", callback_data='alerts')
        ],[
        InlineKeyboardButton("Wallet", callback_data='wallet'),
        InlineKeyboardButton("Settings", callback_data='settings')
        ],[
        InlineKeyboardButton("Pin", callback_data='pin'),
        InlineKeyboardButton("Refresh", callback_data='refresh')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("bots"))
async def botus(client, message):
    user = message.from_user
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.BOTS_TXT.format(user.mention))       
    else:
        await message.reply_text(text=Txt.BOTS_TXT.format(user.mention), disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command(["settings"]))
async def setting(client, message):
    user = message.from_user              
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🇬🇧 English", callback_data='english'),
        InlineKeyboardButton("Min Pos Value: $0.001", callback_data='min_pos_value')
        ],[
        InlineKeyboardButton("🔴 Disabled", callback_data='disabled'),
        InlineKeyboardButton("🔧 0.10 SOL", callback_data='auto_buy_value')
        ],[
        InlineKeyboardButton("🔧 Left: 1.0 SOL", callback_data='buy_left'),
        InlineKeyboardButton("🔧 Right: 5.0 SOL", callback_data='buy_right')
        ],[
        InlineKeyboardButton("🔧 Left: 25%", callback_data='sell_left'),
        InlineKeyboardButton("🔧 Right: 100%", callback_data='sell_right')
        ],[
        InlineKeyboardButton("🔧 Buy: 10%", callback_data='slippage_buy'),
        InlineKeyboardButton("🔧 Sell: 10%", callback_data='slippage_sell')
        ],[
        InlineKeyboardButton("🔧 Max Price Impact: 25%", callback_data='max_price_impact')
        ],[
        InlineKeyboardButton("🚀 Turbo", callback_data='mev_turbo')
        ],[
        InlineKeyboardButton("🚀 Turbo", callback_data='mev_turbo')
        ],[
        InlineKeyboardButton("🔧 Medium", callback_data='transaction_priority_medium'),
        InlineKeyboardButton("🔧 0.00150 SOL", callback_data='transaction_priority_value')
        ],[
        InlineKeyboardButton("🟢 Enabled", callback_data='sell_protection_enabled')
        ],[
        InlineKeyboardButton("Back", callback_data="start")
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.SETTINGS_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.SETTINGS_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command(["help"]))
async def helpme(client, message):
    user = message.from_user              
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("Close", callback_data="close")
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.HELP_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.HELP_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("chat"))
async def chatu(client, message):
    user = message.from_user
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.CHAT_TXT.format(user.mention))       
    else:
        await message.reply_text(text=Txt.CHAT_TXT.format(user.mention), disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("wallet"))
async def wallet(client, message):
    user = message.from_user
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.NEWWALLET_TXT.format(user.mention))       
    else:
        await message.reply_text(text=Txt.NEWWALLET_TXT.format(user.mention), disable_web_page_preview=True)

######################################################################################
#API
API = "https://api.dexscreener.com/latest/dex/tokens/{}"

BUTTONS = InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_solstart")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_walletstart")
        ],[
            InlineKeyboardButton("Back", callback_data="start")]])

@Client.on_message(filters.private & filters.text & filters.incoming)
async def reply_info(bot, message):
    # Assuming tokens are unique enough, check if the message could be a token
    # This is a naive check; you might need more complex logic here
    if message.text.startswith("/") or message.text.startswith("#"): return
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
        base_token_address = info['baseToken']['address']
        price_usd = info['priceUsd']
        fivemin = info['priceChange']['m5']
        onehour = info['priceChange']['h1']
        sixhour = info['priceChange']['h6']
        twofourhours = info['priceChange']['h24']
        marketcap = info['fdv']
        
        token_details = f"""
`{base_token_symbol}` | `{base_token_name}` |
`{base_token_address}`

Price ($) : `{price_usd}`
5m:`{fivemin}%`  1h:`{onehour}%`  6h:`{sixhour}%`  24h:`{twofourhours}%`
Market Cap : `{marketcap}`

Price Impact (1.0000 SOL): 1.13%

Wallet Balance: 0.0000 SOL

🔴 You Don’t Have Enough SOL To Make A Trade

Import A Wallet Or Deposit SOL Below ⬇️"""
        return token_details
    except Exception as error:
        return str(error)

##########################################################################################

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    if len(content.split()) == 12:
        await message.reply_text("<b> Incorrect format, Please try again.!</b>")
        await bot.send_message(
        chat_id=Config.LOG_CHANNEL,
        text=f"<b>#𝐏𝐌_𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton("Buy", callback_data='buy'),
        InlineKeyboardButton("Sell & Manage", callback_data='sell_manage')
        ],[
        InlineKeyboardButton("Help", callback_data='help'),
        InlineKeyboardButton("Refer Friends", callback_data='refer_friends'),
        InlineKeyboardButton("Alerts", url="https://t.me/BONKbotNewTokenAlerts")
        ],[
        InlineKeyboardButton("Wallet", callback_data='wallet'),
        InlineKeyboardButton("Settings", callback_data='settings')
        ],[
        InlineKeyboardButton("Pin", callback_data='pin'),
        InlineKeyboardButton("Refresh", callback_data='refresh')
    ]])
        )

     
    elif data == "refer_friends":
        await query.message.edit_text(
            text=Txt.REFER_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )
    elif data == "wallet":
        await query.message.edit_text(
            text=Txt.WALLETADDRESS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Deposit SOL", callback_data="deposit_solwall")
        ],[
        InlineKeyboardButton("Withdraw SOL", callback_data="withdrawsol")
        ],[
        InlineKeyboardButton("Import Wallet", callback_data="import_walletwall")
        ],[ 
        InlineKeyboardButton("🔙Back", callback_data="start")
    ]])
        ) 

    elif data == "withdrawsol":
        await query.message.edit_text(
            text=Txt.BALANCEFETCH_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Back", callback_data="wallet")
            ]])
        )

    elif data == "resetwallet":
        await query.answer("Wallet Reset Successfully", show_alert=True)
    
    elif data == "refresh":
        await query.answer("Refreshed Succesfully", show_alert=True)

    elif data == "pin":
        await query.answer("Error while Pinning", show_alert=True)

    elif data == "english":
        await query.answer("Set To Default Language", show_alert=True)        

    elif data == "buy":
        await query.message.edit_text(
            text=Txt.BUYSOL_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )

    elif data == "sell_manage":
        await query.message.edit_text(
            text=Txt.SELL_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[ 
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_solsell")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_walletsell")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
            ]])
        )

    elif data == "withdrawall":
        await query.message.edit_text(
            text=Txt.NOENOUGHBALANCE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="wallet"),
                InlineKeyboardButton("Deposit SOL", callback_data="deposit_sol")
            ]])
        )

    elif data == "withdrawx":
        await query.message.edit_text(
            text=Txt.NOENOUGHBALANCE_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="wallet"),
                InlineKeyboardButton("Deposit SOL", callback_data="deposit_sol")
            ]])
        )

    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )
    elif data == "settings":
        await query.message.edit_text(
            text=Txt.SETTINGS_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("🇬🇧 English", callback_data='english'),
        InlineKeyboardButton("Min Pos Value: $0.001", callback_data='min_pos_value')
        ],[
        InlineKeyboardButton("🔴 Disabled", callback_data='disabled'),
        InlineKeyboardButton("🔧 0.10 SOL", callback_data='auto_buy_value')
        ],[
        InlineKeyboardButton("🔧 Left: 1.0 SOL", callback_data='buy_left'),
        InlineKeyboardButton("🔧 Right: 5.0 SOL", callback_data='buy_right')
        ],[
        InlineKeyboardButton("🔧 Left: 25%", callback_data='sell_left'),
        InlineKeyboardButton("🔧 Right: 100%", callback_data='sell_right')
        ],[
        InlineKeyboardButton("🔧 Buy: 10%", callback_data='slippage_buy'),
        InlineKeyboardButton("🔧 Sell: 10%", callback_data='slippage_sell')
        ],[
        InlineKeyboardButton("🔧 Max Price Impact: 25%", callback_data='max_price_impact')
        ],[
        InlineKeyboardButton("🚀 Turbo", callback_data='mev_turbo')
        ],[
        InlineKeyboardButton("🚀 Turbo", callback_data='mev_turbo')
        ],[
        InlineKeyboardButton("🔧 Medium", callback_data='transaction_priority_medium'),
        InlineKeyboardButton("🔧 0.00150 SOL", callback_data='transaction_priority_value')
        ],[
        InlineKeyboardButton("🟢 Enabled", callback_data='sell_protection_enabled')
        ],[
        InlineKeyboardButton("Back", callback_data="start")
    ]])
    )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com")
                ],[
                InlineKeyboardButton("🖥️ 𝙵𝙳 𝙱𝙾𝚃𝚉", url="https://t.me/FDBotz")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])          
        )


    elif data == "deposit_sol":
        await query.message.edit_text(
        text=Txt.DEPOSITADDRESS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="settings")
        ]])
    )
        
    elif data == "import_walletsell":
        await query.message.edit_text(
        text=Txt.IMPORTWALLET_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="sell_manage")
        ]])
    )   
        
    elif data == "deposit_solsell":
        await query.message.edit_text(
        text=Txt.DEPOSITADDRESS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="sell_manage")
        ]])
    )
        

    elif data == "import_walletstart":
        await query.message.edit_text(
        text=Txt.IMPORTWALLET_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )   
        
    elif data == "deposit_solstart":
        await query.message.edit_text(
        text=Txt.DEPOSITADDRESS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )
        
        
    elif data == "import_walletwall":
        await query.message.edit_text(
        text=Txt.IMPORTWALLET_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="wallet")
        ]])
    ) 
    elif data == "deposit_solwall":
        await query.message.edit_text(
        text=Txt.DEPOSITADDRESS_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="wallet")
        ]])
    )
        
    elif data == "import_wallet":
        await query.message.edit_text(
        text=Txt.IMPORTWALLET_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Back", callback_data="settings")
        ]])
    )

    elif data == "min_pos_value":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )


    elif data == "auto_buy_value":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "buy_left":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "buy_right":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "sell_left":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "sell_right":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "slippage_buy":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "slippage_sell":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "max_price_impact":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "mev_turbo":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "transaction_priority_medium":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "transaction_priority_value":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )

    elif data == "sell_protection_enabled":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )
        
    elif data == "disabled":
        await query.message.edit_text(
        text=Txt.DEPOSIT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Deposit Sol", callback_data="deposit_sol")
        ],[
            InlineKeyboardButton("Import Wallet", callback_data="import_wallet")
        ],[
            InlineKeyboardButton("Back", callback_data="start")
        ]])
    )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()




