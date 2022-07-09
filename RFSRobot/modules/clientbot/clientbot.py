from . import queues
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pyrogram import Client as Bot
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from RFSRobot.config import API_ID, API_HASH, STRING_SESSION

client = Bot(
    STRING_SESSION,
    API_ID,
    API_HASH,
    plugins=dict(root="RFSRobot.plugins")
)

pytgcalls = PyTgCalls(client)

@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, 
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )
