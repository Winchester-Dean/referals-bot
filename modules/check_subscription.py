import logging

from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from database.db import DataBase

logging.basicConfig(level=logging.INFO)

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        msg: Message,
        data: Dict[str, Any]
    ) -> Any:
        database = DataBase()
        channels = database.get_channels_id()

        for chid in channels:
            try:
                member = await msg.bot.get_chat_memebr(
                    chid, msg.from_user.id
                )

                if member.status == "left":
                    return await msg.answer(
                        "Пожалуйста подпишитесь на каналы!"
                    )
            except Exception as error:
                logging.error(error)
        
        return await handler(event, data)

