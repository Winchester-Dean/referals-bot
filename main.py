import asyncio
import logging

from dispatcher import dp
from handlers import *

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
