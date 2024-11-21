from typing import Union

from starlette.responses import Response
from fastapi import APIRouter, Depends

from src.models import Product
from src.models.db_config import db_config
from .service import ProductService
from .schemas import SingleProduct, ListProduct

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


# get all active products
@router.get('/all/', summary="Get all products from DB", response_model=Union[list[ListProduct], None])
async def get_all_products(response: Response,
                           session: AsyncSession = Depends(db_config.get_session)) -> list[Product] | Exception:
    """Return all products from DB with Flag Active or raise exception if DB is empty"""
    products = await ProductService.get_all_products(session=session, response=response)
    return products


# get product by id
@router.get('/id/{product_uuid}', summary="Get product by id", response_model=Union[SingleProduct, None])
async def get_product_by_uuid(product_uuid: str, response: Response,
                              session: AsyncSession = Depends(db_config.get_session)) -> Product | Exception:
    """Get id and return product if it exists, else return exception"""
    product = await ProductService.get_product_by_uuid(product_uuid=product_uuid, response=response, session=session)
    return product
