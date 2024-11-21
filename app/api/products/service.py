from sqlalchemy import select, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from src.models import Product


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

    @staticmethod
    async def get_all_products(response: Response, session: AsyncSession) -> list[Product]:
        """Return all products with status is_active"""

        stmt = (select(Product).where(Product.is_active == True).options(
            selectinload(Product.product_brand), selectinload(Product.product_size)).order_by(
            desc(Product.created_at)))
        products = await session.scalars(stmt)
        products = list(products)
        if products:
            response.status = status.HTTP_200_OK
            return list(products)
        raise HTTPException(500, detail='products not found, DB is empty')