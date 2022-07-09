import time
import asyncio
from pyrogram import Client, filters
from RFSRobot.modules.helpers.filters import command
from pyrogram.types import ChatPermissions, Message


@Client.on_message(command("pin") & filters.me)  
async def pin_message(client: Client, message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I pin your head to wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.pin_chat_message(chat_id , reply_msg_id , both_sides=True)
            await message.edit_text("**🥀 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐏𝐢𝐧𝐧𝐞𝐝 💞 ...**")
        else:
            zuzu= await client.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if not can_pin:
                await client.edit_message_text(chat_id , msg_id , "**🥀 𝐈 𝐚𝐦 𝐍𝐨𝐭 𝐚𝐧 𝐀𝐝𝐦𝐢𝐧 ✨ ...**") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.pin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "**🥀 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐏𝐢𝐧𝐧𝐞𝐝 💞 ...**")
