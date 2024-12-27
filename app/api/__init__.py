from .products.views import router as products_router
from .users.views import router as users_router
from .orders.views import router as orders_router

from fastapi import APIRouter

router = APIRouter(prefix='/api')
router.include_router(products_router, prefix='/products', tags=['products'])
router.include_router(users_router)
router.include_router(orders_router, prefix='/orders', tags=['orders'])