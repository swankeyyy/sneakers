from typing import Union

from starlette.responses import Response
from fastapi import APIRouter, Depends

from src.models import Product
from src.models.db_config import db_config
from .service import ProductService
from .schemas import SingleProduct

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get('/{product_uuid}', summary="Get product by id", response_model=Union[SingleProduct, None])
async def get_product_by_uuid(product_uuid: str, response: Response,
                              session: AsyncSession = Depends(db_config.get_session)) -> Product | Exception:
    """Get id and return product if it exists, else return exception"""
    product = await ProductService.get_product_by_uuid(product_uuid=product_uuid, response=response, session=session)
    return product
