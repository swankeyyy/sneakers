import uuid

from fastapi.security import HTTPBearer
from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends

from api.users.schemas import UserUpdate, UserCreate, UserRead

from src.authentication.dependencies import get_user_manager
from src.models.user import User
from src.authentication.backend import auth_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

# add dependency of token input
http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    dependencies=[Depends(http_bearer)],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
