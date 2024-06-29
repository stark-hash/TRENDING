import os
import re
import logging
from pymongo import MongoClient
from pyrogram import Client, filters
from config import Config
from dotenv import load_dotenv
from Script import script


# Setup logging
logging.basicConfig(level=logging.INFO)

# Fetch the MongoDB URI from environment variables
mongo_client = MongoClient(Config.DB_URL)
mongo_db = mongo_client["cloned_fdbotz"]
mongo_collection = mongo_db[Config.DB_NAME]

# Initialize MongoDB client with SSL configuration
try:
    mongo_client = MongoClient(Config.DB_URL, serverSelectionTimeoutMS=5000)
    mongo_db = mongo_client["cloned_fdbotz"]
    mongo_collection = mongo_db["your_collection_name"]
    logging.info("Connected to MongoDB successfully.")
except Exception as e:
    logging.exception("Error connecting to MongoDB: %s", e)
    raise

def is_bot_creator(user_id, bot_token):
    bot = mongo_collection.find_one({"token": bot_token})
    return bot and bot['user_id'] == user_id

@Client.on_message(filters.command("clone") & filters.private)
async def clone(client, message):
    await message.reply_text("Clone command received.")

@Client.on_message(filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}') & filters.private)
async def on_clone(client, message):
    try:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
        bot_token = bot_token[0] if bot_token else None

        bots = list(mongo_db.bots.find())
        bot_tokens = [bot['token'] for bot in bots]

        forward_from_id = message.forward_from.id if message.forward_from else None
        if bot_token in bot_tokens and forward_from_id == 1195233863:
            await message.reply_text("**©️ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ 🐥**")
            return

        if forward_from_id == 1195233863:
            msg = await message.reply_text("**👨‍💻 ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ❣️**")
            try:
                ai = Client(
                    f"{bot_token}", Config.API_ID, Config.API_HASH,
                    bot_token=bot_token,
                    plugins={"root": "clone_plugins"},
                    # Use in-memory storage to avoid SQLite issues
                )


                await ai.start()
                bot = await ai.get_me()
                details = {
                    'bot_id': bot.id,
                    'is_bot': True,
                    'user_id': user_id,
                    'name': bot.first_name,
                    'token': bot_token,
                    'username': bot.username
                }
                mongo_db.bots.insert_one(details)
                await msg.edit_text(f"<b>sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴏɴᴇᴅ ʏᴏᴜʀ ʙᴏᴛ: @{bot.username}.\n\nғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ sᴛᴀʀᴛ ʏᴏᴜʀ ᴄʟᴏɴᴇᴅ ʙᴏᴛ</b>")
            except BaseException as e:
                logging.exception("Error while cloning bot.")
                await msg.edit_text(f"⚠️ <b>Bot Error:</b>\n\n<code>{e}</code>\n\n**Kindly forward this message to @TGTesla to get assistance.**")
    except Exception as e:
        logging.exception("Error while handling message: %s", e)

@Client.on_message(filters.command("deletecloned") & filters.private)
async def delete_cloned_bot(client, message):
    try:
        bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
        bot_token = bot_token[0] if bot_token else None

        cloned_bot = mongo_collection.find_one({"token": bot_token})
        if cloned_bot:
            mongo_collection.delete_one({"token": bot_token})
            await message.reply_text("**🤖 ᴛʜᴇ ᴄʟᴏɴᴇᴅ ʙᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ʟɪsᴛ ᴀɴᴅ ɪᴛs ᴅᴇᴛᴀɪʟs ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ. ☠️**")
        else:
            await message.reply_text("**⚠️ ᴛʜᴇ ʙᴏᴛ ᴛᴏᴋᴇɴ ᴘʀᴏᴠɪᴅᴇᴅ ɪs ɴᴏᴛ ɪɴ ᴛʜᴇ ᴄʟᴏɴᴇᴅ ʟɪsᴛ.**")
    except Exception as e:
        logging.exception("Error while deleting cloned bot.")
        await message.reply_text("An error occurred while deleting the cloned bot.")

async def restart_bot():
    logging.info("Restarting all bots........")
    bots = list(mongo_db.bots.find())
    for bot in bots:
        bot_token = bot['token']
        try:
            ai = Client(
                f"{bot_token}", Config.API_ID, Config.API_HASH,
                bot_token=bot_token,
                plugins={"root": "clone_plugins"},
            )
            await ai.start()
        except Exception as e:
            logging.exception(f"Error while restarting bot with token {bot_token}: {e}")