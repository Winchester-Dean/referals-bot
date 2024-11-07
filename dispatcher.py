import logging

from config import TOKEN
from aiogram import Bot, Dispatcher

from modules.check_subscription import CheckSubscriptionMiddleware

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.setup_middleware(CheckSubscriptionMiddleware())


