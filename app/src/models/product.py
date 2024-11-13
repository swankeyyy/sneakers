from .base import IdPkMixin, Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, validates


class Product(IdPkMixin, Base):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


class Brand(IdPkMixin, Base):
    __tablename__ = 'brands'
    name: Mapped[str] = mapped_column(String(40), unique=True, name="Brand name", nullable=False)


class Size(IdPkMixin, Base):
    __tablename__ = 'sizes'
    size: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    @validates('size')
    def validate_size(self, key, value):
        if not 36 < value < 46:
            raise ValueError(f'Invalid size {value}')
        return value
