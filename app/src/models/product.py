from typing import List

from .base import IdPkMixin, Base

from sqlalchemy import String, Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship
from sqlalchemy.dialects.postgresql import UUID

from enum import Enum as en_Enum


class GenderType(en_Enum):
    male = 'M'
    female = 'F'


class Product(IdPkMixin, Base):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    gender: Mapped[GenderType] = mapped_column(Enum(GenderType), default=GenderType.male)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    slug: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    product_brand_id: Mapped[UUID] = mapped_column(ForeignKey('brands.id'), nullable=False)
    product_brand: Mapped["Brand"] = relationship(back_populates="products")


class Brand(IdPkMixin, Base):
    __tablename__ = 'brands'
    name: Mapped[str] = mapped_column(String(40), unique=True, name="Brand name", nullable=False)
    products: Mapped[List["Product"]] = relationship(back_populates="product_brand",
                                                     cascade="all, delete-orphan", lazy="select")


class Size(IdPkMixin, Base):
    __tablename__ = 'sizes'
    size: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    @validates('size')
    def validate_size(self, key, value):
        if not 36 < value < 46:
            raise ValueError(f'Invalid size {value}')
        return value
