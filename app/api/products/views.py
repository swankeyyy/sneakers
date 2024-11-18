from starlette import status

from src.models.db_config import db_config
from .service import _add_size, _add_brand
from .schemas import SizeBase, BrandBase

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post('/add_new_brand', status_code=status.HTTP_201_CREATED, response_model=BrandBase,
             summary="Add a new brand of sneakers")
async def add_brand(new_brand: str, session: AsyncSession = Depends(db_config.get_session)):
    """Takes name of brand(str) and create new brand"""
    response = await _add_brand(new_brand=new_brand, session=session)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@router.post('/add_new_size', status_code=status.HTTP_201_CREATED, response_model=SizeBase,
             summary="Add a new size of sneaker")
async def add_size(new_size: int, session: AsyncSession = Depends(db_config.get_session)):
    """Takes int and create new size of sneaker"""
    response = await _add_size(new_size=new_size, session=session)
    if response:
        return response
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
