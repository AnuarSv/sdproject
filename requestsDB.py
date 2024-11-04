from models import User
from sqlalchemy import select
from dbinit import async_session

class HistoryService:

    async def save_history(self, tg_id: int, text: str):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if user:
                user.history = (user.history or "") + "\n" + text
                await session.commit()

    async def get_history(self, tg_id: int) -> str:
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if not user:
                session.add(User(tg_id=tg_id))
                await session.commit()
            return user.history if user else "No history"
            
    async def delete_history(self, tg_id: int):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            if user:
                user.history = ""
                await session.commit()
