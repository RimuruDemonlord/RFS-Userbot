from pyrogram import filters
from typing import Union, List
from RFSRobot.config import *

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
rfs_filters = filters.me & filters.user(SUDO_USERS)

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

