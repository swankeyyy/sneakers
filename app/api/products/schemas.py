import uuid
from pydantic import BaseModel, ConfigDict


class SizeSchema(BaseModel):
    id: uuid.UUID
    size: int
    model_config = ConfigDict(
        from_attributes=True
    )
