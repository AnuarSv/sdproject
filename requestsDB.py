from models import User, db
from sqlalchemy import select

async def set_user(tg_id: int):
    async with db.get_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def save_history(tg_id: int, text: str) -> None:
    async with db.get_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            user.history = (user.history or "") + "\n" + text
            await session.commit()

async def get_history(tg_id: int) -> str:
    async with db.get_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user.history if user and user.history else "None"

async def delete_history(tg_id: int) -> str:
    async with db.get_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user:
            user.history = ""
            await session.commit()
            return "Done"
