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

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))



class Txt(object):
    # part of text configuration
    START_TXT = """Finder Trending Boost  // 

⚡️ Guaranteed Trending

💎 Increase volume & visibility for your token 

➤ type /trending to get started"""

    TRENDING_TXT = """Reply to this message with the CA of the token you would like to purchase Finder Trending for"""

    THREEHRS_TXT = """Send <code>3</code> SOL to the wallet below 

<code>3ifctTLij3LsEHbpN3r4hEdPDpSUdeJLWL8GVT946q1b</code>

Click "Paid" once sent to scan for transaction. Once detected trending will begin shortly."""

    SIXHRS_TXT = """Send <code>5.5</code> SOL to the wallet below 

<code>3ifctTLij3LsEHbpN3r4hEdPDpSUdeJLWL8GVT946q1b</code>

Click "Paid" once sent to scan for transaction. Once detected trending will begin shortly."""

    TWELVEHRS_TXT = """Send <code>11</code> SOL to the wallet below 

<code>3ifctTLij3LsEHbpN3r4hEdPDpSUdeJLWL8GVT946q1b</code>

Click "Paid" once sent to scan for transaction. Once detected trending will begin shortly."""

    TWOFOURHRS_TXT = """Send <code>17</code> SOL to the wallet below 

<code>3ifctTLij3LsEHbpN3r4hEdPDpSUdeJLWL8GVT946q1b</code>

Click "Paid" once sent to scan for transaction. Once detected trending will begin shortly."""

    PAYMENT_TXT = """Payment not detected, if already sent try again in a minute"""
    
    
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


