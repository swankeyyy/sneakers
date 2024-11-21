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


class ListProduct(ProductBase):
    """Schema for list of products with status active"""
    name: str
    slug: str
    image: Optional[str] = None
    price: int
    product_brand: BrandBase


class ListBrands(BrandBase):
    """Schema for list of brands with active products"""
    products: list[ListProduct]
