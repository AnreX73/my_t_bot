import asyncio
from aiogram import Bot, Dispatcher, types

bot = Bot(token="")
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message):
    await message.answer(f'{message.text} чё надо ?')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
