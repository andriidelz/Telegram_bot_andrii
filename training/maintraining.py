import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold

from token_api import TOKEN_API


dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    reply_text = f'Hello, {hbold(msg.from_user.full_name)}. It has commands /help, '
    await msg.answer(text=reply_text)


@dp.message(Command(commands=['help']))
async def help(msg: types.Message) -> None:
    await msg.answer(text=f'This bot cannot do everying and nothing')


async def main() -> None:
    bot = Bot(token=TOKEN_API,
              parse_mode='HTML'
              )   
    await dp.start_polling(bot)


#     logging.basicConfig(
#     format='%(levelname)s: %(message)s',
#     level=logging.INFO,
#     filename='app.log',
#     filemode='w'
# )
    
if __name__ == '__main__':
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
    asyncio.run(main())