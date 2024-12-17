import uuid
from typing import List, Optional

from fastapi_users import schemas
from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    id: uuid.UUID
    model_config = ConfigDict(
        from_attributes=True
    )


class ProductInOrder(Base):
    name: str


class Order(Base):
    products: Optional[List[ProductInOrder]] = None


class UserRead(schemas.BaseUser[uuid.UUID]):
    orders: Optional[List[Order]] = None


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
