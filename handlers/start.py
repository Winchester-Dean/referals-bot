import logging

from dispacher import dp
from aioram.types import Message
from aioram.filters.command import Command

logging.baseConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Ну привет")
