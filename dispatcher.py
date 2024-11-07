import logging

from config_reader import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from modules.check_subscription import CheckSubscriptionMiddleware

logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=config.bot_token.get_secret_value()
)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.setup_middleware(CheckSubscriptionMiddleware())


