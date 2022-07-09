# Copyright (C) 2022 By AdityaHalder // RFSRobot

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from RFSRobot.modules.helpers.filters import *
from RFSRobot.modules.helpers.decorators import sudo_users_only, errors
from RFSRobot.plugins.help import *

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & rfs_filters)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **deleted all downloaded files**")
    else:
        await message.reply_text("❌ **no files downloaded**")

        
@Client.on_message(command(["rmw", "clean"]) & rfs_filters)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **deleted all raw files**")
    else:
        await message.reply_text("❌ **no raw files**")


@Client.on_message(command(["cleanup"]) & rfs_filters)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **cleaned**")
    else:
        await message.reply_text("✅ **already cleaned**")


add_command_help(
    "animation",
    [
        [
            ".rmd",
            "To Clean All Junk Downloaded Files."
        ],
        [
            ".rmw",
            "To Clean All Junk Raw Files."
        ],
        [
            ".cleanup",
            "To Clean All Junk Images.",
        ],

    ],
)