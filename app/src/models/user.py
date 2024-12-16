from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base

from fastapi_users.db import SQLAlchemyBaseUserTableUUID

if TYPE_CHECKING:
    from .order import Order


class User(SQLAlchemyBaseUserTableUUID, Base):
    orders: Mapped[List["Order"]] = relationship(back_populates="order_user",
                                                 cascade="all, delete-orphan", lazy="select")
