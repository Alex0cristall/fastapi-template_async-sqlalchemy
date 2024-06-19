from sqlalchemy import MetaData
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)

from core.config import settings
from utils import camel_case_to_snake_case



class Base(DeclarativeBase):
    __abstract__ = True
    
    metadata = MetaData(
        naming_convention=settings.db.convention
    )
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return camel_case_to_snake_case(cls.__name__)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
