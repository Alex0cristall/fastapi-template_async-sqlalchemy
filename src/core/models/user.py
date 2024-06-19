from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DefaultUserData(Base):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
