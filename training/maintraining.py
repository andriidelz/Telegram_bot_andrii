import asyncio
import logging

from token_api import TOKEN_API
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

token = "6900592213:AAHJTfRX2vYdnmYivJh3vAXWloPqEaBKsX4"
dp = Dispatcher()

@dp.message(CommandStart())
async def cdm_start(msg: types.Message) -> None:
    await msg.answer(
        text = 'Hello World!'
    )

async def main() -> None:
    bot = Bot(TOKEN_API)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
    asyncio.run(main()) 