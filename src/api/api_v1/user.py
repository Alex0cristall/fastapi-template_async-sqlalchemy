from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.user import UserRead, UserCreate
from crud.user import get_all_user, insert_user
from core.models import db_helper



router = APIRouter(tags=['User'])


@router.get('/', response_model=list[UserRead])
async def get_users(session: Annotated[AsyncSession, Depends(db_helper.session_getter)]):
    users = await get_all_user(session)
    return users


@router.post('/create_user/', response_model=UserRead)
async def create_user(
    user: UserCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    user_created = await insert_user(session, user)
    return user_created
