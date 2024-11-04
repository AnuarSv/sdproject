# adapter
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from config import BOT_TOKEN

class Adapter:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.dp = Dispatcher()

    async def start(self, router):
        self.dp.include_router(router)
        await self.dp.start_polling(self.bot)

    async def send(self, chat_id: int, text: str, reply_markup=None):
        await self.bot.send_message(chat_id, text, reply_markup=reply_markup)

    async def reply(self, message: Message, text: str):
        await message.reply(text)
