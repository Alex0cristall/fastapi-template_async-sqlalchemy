from typing import Sequence

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.user import UserCreate
from core.models import DefaultUserData



async def get_all_user(session: AsyncSession) -> Sequence[DefaultUserData]:
    stmt = select(DefaultUserData).order_by(DefaultUserData.id)

    result = await session.scalars(stmt)
    return result.all()


async def insert_user(session: AsyncSession, user_create: UserCreate) -> None:
    user = DefaultUserData(**user_create.model_dump())
    session.add(user)

    await session.commit()
    # await session.refresh()
    
    return user
    
