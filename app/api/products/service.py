from .schemas import SizeSchema
from src.models import Size

from sqlalchemy.ext.asyncio import AsyncSession


async def _add_size(new_size: int, session: AsyncSession) -> Size:
    size = Size(size=new_size)
    session.add(size)
    await session.commit()
    await session.refresh(size)
    return size
