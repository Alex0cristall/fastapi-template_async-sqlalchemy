from fastapi import APIRouter

from .user import router as router_user
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.prefix
)
router.include_router(
    router=router_user,
    prefix=settings.api.v1.user
)
 