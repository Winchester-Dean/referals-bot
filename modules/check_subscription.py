import logging

from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from database.db import DataBase

logging.basicConfig(level=logging.INFO)

database = DataBase()

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def add_user_db(
        self,
        user_id: int,
        name: str
    ):
        users = database.get_users_id()
        for user in users:
            if user_id != user[0]:
                database.add_user(
                    user_id, name
                )

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        msg: Message,
        data: Dict[str, Any]
    ) -> Any:
        channels = database.get_channels_id()

        for chid in channels:
            try:
                member = await msg.bot.get_chat_member(
                    f"-100{chid[0]}", msg.from_user.id
                )

                if member.status == "left":
                    return await msg.answer(
                        "Пожалуйста подпишитесь на каналы!"
                    )
            except Exception as error:
                logging.error(error)
        
        await self.add_user_db(
            msg.from_user.id,
            msg.from_user.first_name
        )

        return await handler(msg, data)

