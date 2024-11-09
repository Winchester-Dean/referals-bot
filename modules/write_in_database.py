import logging

from aiogram.types import Message
from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from database.db import DataBase

database = DataBase()

class WriteInDatabaseMiddleware(BaseMiddleware):
    def __call__(
        self,
        handler: Callable[
            [Message, Dict[str, Any]],
            Awaitable[Any]
        ],
        msg: Message,
        data: Dict[str, Any]
    ) -> Any:
        users = database.get_users_id()
        user_id = msg.from_user.id
        name = msg.from_user.first_name
        args = msg.text.split(maxsplit=1)

        if len(args) > 1
            referer_id = args[1]
            if referer_id.isdigit():
                referer_id = int(referer_id)
                referer = True
        else:
            referer = False

        if data["subscribed"]:
            for user in users:
                if (user_id,) not in user:
                    if referer:
                        database.add_user(
                            user_id, name, referer_id
                        )
                    else:
                        database.add_user(
                            user_id, name
                        )

