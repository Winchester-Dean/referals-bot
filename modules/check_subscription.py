import logging

from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from database.db import DataBase

from handlers.keyboards.keyboard import inline_channels

logging.basicConfig(level=logging.INFO)

database = DataBase()

class CheckSubscriptionMiddleware(BaseMiddleware):
    def __call__(
        self,
        handler: Callable[
            [Message, Dict[str, Any]],
            Awaitable[Any]
        ],
        msg: Message,
        data: Dict[str, Any]
    ) -> Any:
        channels = database.get_channels_id()

        for chid in channels:
            try:
                member = await msg.bot.get_chat_memeber(
                    f"-100{chid[0]}",
                    msg.from_user.id
                )

                if member.status != "left":
                    data["subscribed"] = True
                else:
                    data["subscribed"] = False
                    return await msg.answer(
                        "Пожалуйста подпишитесь на каналы:",
                        reply_markup = inline_channels
                    )
            except Exception as error:
                logging.error(error)

        return await handler(msg, data)


