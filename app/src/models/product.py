from datetime import datetime
from typing import List, TYPE_CHECKING
from uuid import UUID

from app.src.settings import settings
from .base import IdPkMixin, Base


from sqlalchemy import String, Integer, Enum, ForeignKey, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, validates, relationship

from fastapi_storages.integrations.sqlalchemy import FileType
from fastapi_storages import FileSystemStorage

from enum import Enum as en_Enum

if TYPE_CHECKING:
    from .order import Order

# storage for images of Product
storage = FileSystemStorage(path=settings.STORAGE_URL)


class GenderType(en_Enum):
    """Gender type for sneakers"""
    male = 'M'
    female = 'F'


class Product(IdPkMixin, Base):
    """Product model with size brand and etc"""
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    slug: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    image: Mapped[str] = mapped_column(FileType(storage=storage), nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    gender: Mapped[GenderType] = mapped_column(Enum(GenderType), default=GenderType.male)
    product_size_id: Mapped[UUID] = mapped_column(ForeignKey('sizes.id'), nullable=True)
    product_size: Mapped["Size"] = relationship(back_populates="products")
    product_brand_id: Mapped[UUID] = mapped_column(ForeignKey('brands.id'), nullable=True)
    product_brand: Mapped["Brand"] = relationship(back_populates="products")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.now)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=True)
    orders: Mapped[list["Order"]] = relationship(secondary="order_product_association",
                                                 back_populates="products",
                                                 )

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Brand(IdPkMixin, Base):
    """Brand model for product like adidas puma and etc"""
    __tablename__ = 'brands'
    name: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    products: Mapped[List["Product"]] = relationship(back_populates="product_brand",
                                                     cascade="all, delete-orphan", lazy="select")

    def __repr__(self):
        return self.name


class Size(IdPkMixin, Base):
    """Size model for product like 38 41 42"""
    __tablename__ = 'sizes'
    size: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    products: Mapped[List["Product"]] = relationship(back_populates="product_size",
                                                     cascade="all, delete-orphan", lazy="select")

    def __repr__(self):
        return f'{self.size}'

    def __str__(self):
        return f'{self.size}'

    @validates('size')
    def validate_size(self, key, value):
        if not 36 < value < 46:
            raise ValueError(f'Invalid size {value}')
        return value
