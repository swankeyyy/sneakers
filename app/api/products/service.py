from sqlalchemy import select, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from src.models import Product, Brand


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

        stmt = select(Product).where(Product.is_active == True).options(
            selectinload(Product.product_brand), selectinload(Product.product_size)).order_by(
            desc(Product.created_at))
        products = await session.scalars(stmt)
        products = list(products)
        if products:
            response.status = status.HTTP_200_OK
            return list(products)
        raise HTTPException(500, detail='products not found, DB is empty')

    @staticmethod
    async def get_products_by_size(size: int, response: Response, session: AsyncSession) -> list[Product]:
        """Take size(int) and return all sneakers with that size"""
        stmt = select(Product).options(
            selectinload(Product.product_brand),
            selectinload(Product.product_size)
            ).filter(Product.product_size.has(size=size))
        products = await session.scalars(stmt)
        products = list(products)
        if products:
            response.status = status.HTTP_200_OK
            return list(products)
        raise HTTPException(500, detail='products not found')


class BrandService:
    """All methods related to Brand model"""

    @staticmethod
    async def get_all_brands(response: Response, session: AsyncSession) -> list[Brand]:
        """Return list of all brands with list of products"""
        stmt = select(Brand).options(
            joinedload(Brand.products).selectinload(Product.product_size)).filter(Product.is_active == True)
        brands = await session.execute(stmt)
        brands = brands.scalars().unique().all()
        brands = list(brands)
        if brands:
            response.status = status.HTTP_200_OK
            return brands
        raise HTTPException(500, detail='brands not found, DB is empty')

    @staticmethod
    async def get_brand_by_uuid(brand_uuid: str, response: Response, session: AsyncSession) -> Brand:
        """Return brands by uuid if it exists, else return HTTPError"""
        try:
            stmt = select(Brand).where(Brand.id == brand_uuid).options(
                joinedload(Brand.products).selectinload(Product.product_size)).filter(Product.is_active == True)
            brand = await session.scalar(stmt)
            if brand:
                response.status = status.HTTP_200_OK
                return brand
        except SQLAlchemyError:
            raise HTTPException(500, detail='wrong uuid length')
        raise HTTPException(500, detail='brand not found')
