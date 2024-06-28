from src.facades import db_gateway


async def register_user(chat_id: int) -> None:
    async with db_gateway.create_session() as session:
        if not await db_gateway.has_user_with(chat_id, session=session):
            await db_gateway.register_user(chat_id, session=session)
            await session.commit()


async def get_all_chat_ids() -> list[int]:
    async with db_gateway.create_session() as session:
        return await db_gateway.get_all_chat_ids(session=session)
