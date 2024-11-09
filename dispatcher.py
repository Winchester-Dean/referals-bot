import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from modules.check_subscription import CheckSubscriptionMiddleware, WriteInDatabaseMiddleware

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.outer_middleware(CheckSubscriptionMiddleware())
dp.callback_query.outer_middleware(CheckSubscriptionMiddleware())

dp.message.outer_middleware(WriteInDatabaseMiddleware())
dp.callback_query.outer_middleware(WriteInDatabaseMiddleware())
