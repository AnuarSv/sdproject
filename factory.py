from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import BOT_TOKEN
from models import Base


class Factory:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.dispatcher = Dispatcher()

        self.engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def setup_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def get_bot(self):
        return self.bot

    def get_dispatcher(self):
        return self.dispatcher

    def get_session(self):
        return self.async_session()
