from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
from starlette import status
from starlette.responses import Response

from src.models import Product

from sqlalchemy.ext.asyncio import AsyncSession


class ProductService:
    """All methods related to product service like get product by id, get all products and etc"""

    @staticmethod
    async def get_product_by_uuid(product_uuid: str, response: Response, session: AsyncSession) -> Product:
        """Return product by uuid if it exists, else return HTTPError"""
        try:
            stmt = select(Product).where(product_uuid == Product.id).options(selectinload(Product.product_brand),
                                                                             selectinload(Product.product_size))
            product = await session.scalar(stmt)
            if product:
                response.status = status.HTTP_200_OK
                return product
        except SQLAlchemyError:
            raise HTTPException(500, detail='wrong uuid length')

        raise HTTPException(500, detail='product not found')