import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    """Base model with id"""
    id: uuid.UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class SizeBase(Base):
    size: int


class BrandBase(Base):
    name: str


class ProductBase(Base):
    name: str


class SingleProduct(ProductBase):
    """Schema for single product, got by uuid"""
    description: Optional[str] = None
    slug: str
    image: Optional[str] = None
    quantity: int
    price: float
    gender: str
    created_at: datetime
    product_size: SizeBase
    product_brand: BrandBase
