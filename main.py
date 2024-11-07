import asyncio
import logging

from dispatcher import dp
from handlers import *

logging.basicConfig(level=logging.INFO)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
