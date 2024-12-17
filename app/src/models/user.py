from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base

from fastapi_users.db import SQLAlchemyBaseUserTableUUID

if TYPE_CHECKING:
    from .order import Order


class User(SQLAlchemyBaseUserTableUUID, Base):
    """Default User model of FastapiUsers extended with order"""
    orders: Mapped[List["Order"]] = relationship(back_populates="order_user",
                                                 cascade="all, delete-orphan", lazy="selectin")

    def __repr__(self) -> str:
        return f"<User {self.email}>"