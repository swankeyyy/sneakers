from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from typing import TYPE_CHECKING, Union

from api.users.views import fastapi_users
from src.models import User
from src.models.db_config import db_config
from .schemas import OrderSchema
from .service import OrderService

from src.models.order import Order

current_user = fastapi_users.current_user()

router = APIRouter()


@router.get("/add_product/{product_uuid}", summary="Add a product to order",
            response_model=Union[OrderSchema, None])
async def root(product_uuid: str, response: Response,
               user: User = Depends(current_user),
               session: AsyncSession = Depends(db_config.get_session),
               ) -> Order | Exception:
    """Takes current user by token, add product to order by id"""
    result = await OrderService.add_product(product_uuid, response, user, session)
    return result
