import logging

from aiogram.types import Message
from aiogram import BaseMiddleware

from database.db import DataBase

logging.basicConfig(level=logging.INFO)

database = DataBase()
channels_id = database.get_channels_id()

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_process_message(
        self,
        msg: Message,
        data: dict
    ):
        try:
            for chid in channels_id:
                member = await msg.bot.get_chat_member(
                    chid, msg.from_user.id
                )

                if member.status in ["left", "kicked"]:
                    return await msg.answer(
                        "Пожалуйста подпишитесь на каналы!"
                    )
        except Exception as error:
            logging.error(errot)
