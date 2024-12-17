from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey

from datetime import datetime

from .base import Base, IdPkMixin

if TYPE_CHECKING:
    from .user import User
    from .product import Product


class Order(IdPkMixin, Base):
    """Model of order with FK on User and m2m for products"""
    __tablename__ = 'orders'
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    order_user_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'), nullable=True)
    order_user: Mapped["User"] = relationship(back_populates="orders")
    is_active: Mapped[bool] = mapped_column(default=True, )

    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_association",
        back_populates="orders",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Order {self.id}>"
