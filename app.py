import asyncio
from aiogram import Bot, Dispatcher, types

bot = Bot(token="6920735411:AAGfY0CSe-e-PEnjmsR8SZ6MPm4yxNKadhE")
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message):
    await message.answer(f'{message.text} чё надо ?')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
