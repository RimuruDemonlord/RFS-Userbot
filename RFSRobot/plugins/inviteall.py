import asyncio
from pyrogram import Client, filters 
from pyrogram.types import Message
from RFSRobot.modules.helpers.filters import *
from RFSRobot.modules.helpers.decorators import sudo_users_only, errors
from RFSRobot.plugins.help import *



@Client.on_message(command(["inviteall", "kidnapall"]) & rfs_filters)
@errors
@sudo_users_only
async def inviteall(client: Client, message: Message):
    kaal = await message.reply_text("🤖 Give Title also\n ex: /inviteall @testing")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await kaal.edit_text(f"inviting users from {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()


add_command_help(
    "inviteall",
    [
        [".inviteall", "add members from others group"],
    ],
)
