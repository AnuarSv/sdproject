import asyncio
from aiogram import Dispatcher
from bot import bot
from handlers import router
from dbinit import init_db

async def main():
    await init_db()
    print("BD inited")
    dp = Dispatcher()
    dp.include_router(router)
    print("Handlers connected")
    print("Bot start and ready!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
