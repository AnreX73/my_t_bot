import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

bot = Bot(token="", parse_mode="HTML")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(massage: Message):
    await massage.answer(f"Hello <b>{massage.from_user.first_name}</b>")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
