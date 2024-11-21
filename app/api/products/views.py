from typing import Union

from starlette.responses import Response
from fastapi import APIRouter, Depends

from src.models import Product, Brand
from src.models.db_config import db_config
from .service import ProductService, BrandService
from .schemas import SingleProduct, ListProduct, ListBrands

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


# get all active products brand
@router.get('/brands/all/', summary='Get all brands with list of active products',
            response_model=Union[list[ListBrands, None]])
async def get_all_brands(response: Response,
                         session: AsyncSession = Depends(db_config.get_session)) -> list[Brand] | Exception:
    """Returns all brands with list of active products"""
    brands = await BrandService.get_all_brands(response=response, session=session)
    return brands


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
