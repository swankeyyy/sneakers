from fastapi import HTTPException
from sqlalchemy import select
from starlette import status

from src.models import Product, User, Order


class OrderService:
    @staticmethod
    async def add_product(product_uuid, response, user, session):
        try:
            stmt = select(Product).where(Product.id == product_uuid)
            product = await session.scalar(stmt)
            order = Order(order_user=user)
            order.products.append(product)
            session.add(order)
            await session.commit()
            print(order)
            # order = await session.refresh(order)
            if order:
                response.status = status.HTTP_200_OK
                return order
        except Exception:
            raise HTTPException(500, detail='smth goes wrong')
