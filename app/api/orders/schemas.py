import uuid
from typing import List

from pydantic import BaseModel, ConfigDict

from api.products.schemas import ListProduct


class OrderSchema(BaseModel):
    id: uuid.UUID
    model_config = ConfigDict(
        from_attributes=True
    )
    # is_active: bool
    # products: List[ListProduct]
