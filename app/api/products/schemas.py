import uuid
from pydantic import BaseModel, ConfigDict


class SizeBase(BaseModel):
    id: uuid.UUID
    size: int
    model_config = ConfigDict(
        from_attributes=True
    )

class BrandBase(BaseModel):
    id: uuid.UUID
    name: str
    model_config = ConfigDict(
        from_attributes=True
    )
