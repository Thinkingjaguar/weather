from aiogram import Bot, Dispatcher
import asyncio
from config import TOKEN
from hadlers import FSM


bot = Bot(token=TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(FSM.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
