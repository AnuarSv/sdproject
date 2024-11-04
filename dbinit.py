from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from config import DATABASE_URL
from models import Base

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
