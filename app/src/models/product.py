from .base import IdPkMixin, Base

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Product(IdPkMixin, Base):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String, nullable=False)
