from sqlalchemy import select, insert, exists
from sqlalchemy.ext.asyncio import AsyncSession

from src.periphery.db import tables, sessions


def create_session() -> AsyncSession:
    return sessions.postgres_session_factory()


async def register_user(chat_id: int, *, session: AsyncSession) -> None:
    stmt = insert(tables.User).values(chat_id=chat_id)
    await session.execute(stmt)


async def has_user_with(chat_id: int, *, session: AsyncSession) -> bool:
    query = select(exists(1).where(tables.User.chat_id == chat_id))

    result = await session.scalar(query)
    return bool(result)


async def get_all_chat_ids(*, session: AsyncSession) -> list[int]:
    query = select(tables.User.chat_id)
    results = await session.scalars(query)

    return results.all()
