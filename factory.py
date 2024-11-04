from aiogram import Bot, Dispatcher
from config import BOT_TOKEN


class Factory:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.dispatcher = Dispatcher()

    def get_bot(self):
        return self.bot

    def get_dispatcher(self):
        return self.dispatcher
