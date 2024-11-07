import logging

from dispatcher import dp
from aiogram.types import Message
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Ну привет")
