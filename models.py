from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
# singleton
class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
            cls._instance.async_session = async_sessionmaker(cls._instance.engine)
        return cls._instance

    def get_session(self):
        return self._instance.async_session

db = Database()  # Singleton instance

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    history: Mapped[str] = mapped_column(Text, nullable=True)

async def async_main():
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
