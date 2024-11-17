from src.models import Size, Brand

from sqlalchemy.ext.asyncio import AsyncSession


async def _add_size(new_size: int, session: AsyncSession) -> Size:
    """Create a new size and add it to the database. Got int, return new size"""
    size = Size(size=new_size)
    session.add(size)
    await session.commit()
    await session.refresh(size)
    return size


async def _add_brand(new_brand: str, session: AsyncSession) -> Brand:
    """Create a new brand and add it to the database. Got brand name(str), return new brand"""
    brand = Brand(name=new_brand)
    session.add(brand)
    await session.commit()
    await session.refresh(brand)
    return brand