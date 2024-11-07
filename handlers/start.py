from aiogram.types import Message
from aiogram.filters import Command
from dispatcher import dp


@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Ну привет")
