# Copyright Â© By @RimuruDemonlord // @AdityaHalder
import asyncio
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from RFSRobot.config import *
from RFSRobot.plugins.help import *
from RFSRobot.plugins.cache.data import *
from RFSRobot.modules.helpers.filters import *

Kaal = f"**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**\n\n"
Kaal += f"âââââââââ¯â¢â°ââââââââ\n"
Kaal += f"â  **á´Êá´Êá´É´ á´ á´ÊsÉªá´É´** : `5.0 beta`\n"
Kaal += f"â  **á´ÊÊá´É¢Êá´á´ á´ á´ÊsÉªá´É´** : `{__version__}`\n"
Kaal += f"â  **á´ á´ÊsÉªá´É´**  : `{2.0}`\n"
Kaal += f"â  **Group** : [âðð¥ð¢ðð¤â](https://t.me/RFS_Support)\n"
Kaal += f"âââââââââ®â¢â­ââââââââ\n\n"
Kaal += f"â  **ðÊÇÓÉ ÊÖÊÊ ÖÕ¡Õ¼ ð:** [âðð¥ð¢ðð¤â](https://gitHub.com/RimuruDemonlord/RFS-Userbot)"


usage = f"** â Wrong Usage â** \n Type `.help advanced`"

import os
import sys


@Client.on_message(command(["help"]) & rfs_filters)
async def help(_, e: Message):
        kaal = e.text.split(" ")
        if len(kaal) > 1:
            helping = kaal[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            elif helping.lower() == "replyraid":
                await e.reply(rraid_help)
            elif helping.lower() == "inviteall":
                await e.reply(invite_help)
            elif helping.lower() == "broadcast":
                await e.reply(cast_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
ââââââââââââ
**â Spam Cmds â¢**

â**spam**: Spams a message for given counter (no Count limit)
syntax:
â£ .spam "count" "message to spam"

â**delayspam**: Delay spam a text for given counter after given time.
syntax:
â£ .delayspam "delay time(seconds)" "count" "message to spam"

â**Fast Spam**: Fast Spam a message for given counter (no Count limit)
syntax:
â£ .fspam "count" "message to spam"
 

â**pornspam**: Porn Spam for given counter.
syntax:
â£ .pornspam "counter"

â**raid:** Activates raid on any individual user for given range.
syntax:
â£ .raid "count" "username or user id"

â **Hang:** Hang Message Spam
syntax:
â£ .hang "counts"
â **Eye:** Eye Abuse editings
syntax:
â£ `.eye`

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""


dm_help = f"""
ââââââââââââ
â**â¢ Dm Cmds â¢**

**Warningâ ï¸:**This Plugin Can a Abuse And Harassment With A User!
â**Dm:** Dm to any individual using spam bots
command:
â£ .dm "username or user id" "message"

â **Dm Spam:** Spam in Dm of Any individual Users
command:
â£ .dmspam "username or user id" "count"  "message to spam"

â**Dm Raid:** raid in Dm of Any individual Users
â£ .dmraid "count" "username or user id"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""


join_help = f"""
ââââââââââââ
**â Join Cmds â¢**

â£.join "private/public Chat invite link or username"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

leave_help = f"""
ââââââââââââ
**â Leave Cmds â¢**

â£ `.leave` "group Username or chat user id"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""


cast_help = f"""
ââââââââââââ
**â Broadcast Cmds â¢**
â **Broadcast**: To Broadcast a message Globally.

â£ `.broadcast` "Reply to a message"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

invite_help = f"""
ââââââââââââ
**â inviteall Cmds â¢**
**Warning â ï¸:** inviting stuffs affect ur id do it own risk

**Inviteall:**To inviteall only active members.
Specially designed for inviting active members.

â£ `.inviteall` "group Username or chat user id"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

userbot_help = f"""
ââââââââââââ
**â Userbot Cmds â¢**

â£ .ping : To check Ping 

â£ .alive : To check Bot Awake or not

â£ .restart : To Restart Your Bots

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

rraid_help = f"""
ââââââââââââ
**â ReplyRaid Cmds â¢**

**Warning â ï¸:** This Plugin Can a Abuse And Harassment With A User!
command:
  â£`.replyraid` "userid To activate replyraid (abusive words)"
  â£`.dreplyraid` "userid To deactivate replyraid (abusive words)"


**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

owner_help = f"""
ââââââââââââ
**Profile:** Profile And Other Cmds
commands:

1) .setname "Profile Name"
2) .setbio "coustom Bio"
3) .setpic "reply to media"

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

help_menu = f"""
ââââââââââââ
â**There are following categories**

â£`owner` : Get all owner commands and its usage
â£`spam` : Get all spam commands and its usage
â£`dm` : Get all dm commands and its usage
â£`join` : Get join commands and its usage
â£`leave` : Get leave commands and its usage
â£`userbot` : Get all userbot commands
â£`replyraid` : Get all replyraids commands
â£`inviteall` : Get all inviting commands
â£`broadcast` : Get all globally commands

â**Type** .help "category" **to get all syntax in that category and its usage**
â**Example**: `.help replyraid`

**ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§**
ââââââââââââ
"""

@Client.on_message(command(["delayspam"]) & rfs_filters)
async def delayspam(xspam: Client, e: Message): 
    kkk = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Kaal = kkk[1:]
    if len(Kaal) == 2:
       counts = int(Kaal[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Kaal[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!**")
       sleeptime = float(Kaal[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(sleeptime)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(sleeptime)
    else:
        await e.reply_text("Usage: .delayspam time count message")


@Client.on_message(command(["pornspam"]) & rfs_filters)
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[0]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    kkk = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)
         if ".mp4" in prn or ".MP4," in prn:
              await xspam.send_video(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)


@Client.on_message(command(["ping"]) & rfs_filters)
async def oahgfg(xspam: Client, e: Message):
      await e.reply_text(f"âââââââââââââââââââ\n ê§ ðRFS ÏÑÑÑÐ²ÏÑðê§ \nâââââââââââââââââââ")


@Client.on_message(command(["broadcast"]) & rfs_filters)
async def ossgvskvc(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Reply to a message to broadcast it")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")

@Client.on_message(command(["hang"]) & rfs_filters)
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    rizoel = "âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°ðê°ê°ê°ê°ê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°ðê°ê°ê°ê°ê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°ðê°ê°ê°ê°ê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°ðê°ê°ê°ê°ê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°âê°âê°âê°ê°"
    count = int(counts)
    for _ in range(count):
         await xspam.send_message(e.chat.id, rizoel)
         await asyncio.sleep(0.3)

@Client.on_message(command(["rfs"]) & rfs_filters)
async def hello(client: Client, message: Message):
    await client.send_photo(message.chat.id, ALIVE_IMAGE, caption=Kaal)


@Client.on_message(command(["join"]) & rfs_filters)
async def jhoin(client: Client, message: Message):
    kaal = message.text[6:]
    count = 0
    if not kaal:
        return await message.reply_text("Need a chat username or invite link to join.")
    if kaal.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(kaal)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(command(["leave"]) & rfs_filters)
async def leasse(client: Client, message: Message):
    kaal = message.text[6:]
    count = 0
    if not kaal:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if kaal.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(kaal)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(command(["spam"]) & rfs_filters)
async def skkkspam(client: Client, message: Message):
    sex  = await message.reply_text("â¡ Usage:\n /spam 10 Kkkk ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    if re.search(Owners.lower(), msg.lower()):
        return await e.reply("**Sorry !!**")
    if int(message.chat.id) in GROUP:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await sex.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(command(["raid"]) & rfs_filters)
async def raid(xspam: Client, e: Message):  
      Kaal = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Kaal) == 2:
          counts = int(Kaal[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Kaal[1])
          id = ok.id
          try:
              userz = await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(REPLY_RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          counts = int(Kaal[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          try:
              userz = await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(REPLY_RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .raid count username")


add_command_help(
    "advanced",
    [
        [".delayspam", "<count and text>`."],
        [".raid", "<user id and count>`."],
        [".pornspam", "<count>`."],
    ],
)
