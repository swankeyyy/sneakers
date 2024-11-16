from starlette import status

from src.models.db_config import db_config
from src.models import Product, Brand, Size
from .service import _add_size
from .schemas import SizeSchema

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()



@router.post('/add_brand')
async def add_brand(brand: str,  session: AsyncSession = Depends(db_config.get_session)):
    item = Brand(name=brand)
    session.add(item)
    await session.commit()
    return item


@router.post('/add_new_size/', status_code=status.HTTP_201_CREATED, response_model=SizeSchema,
             summary="Add a new size of sneaker")
async def add_size(new_size: int, session: AsyncSession = Depends(db_config.get_session)):
    """Takes int and create new size of sneaker"""
    response = await _add_size(new_size=new_size, session=session)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)