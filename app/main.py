from fastapi import FastAPI

import uvicorn

from contextlib import asynccontextmanager

from api import router as api_router
from src.admin.config import create_admin
from src.models.db_config import db_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """close DB after lifespan"""
    yield
    await db_config.dispose()


main_app = FastAPI(lifespan=lifespan, title='Sneakers shop',
                   description="prjct for learn FastAPI",
                   version='0.0.1',
                   contact={
                       "name": "Ivan Levchuk",
                       "email": "swankyyy1@gmail.com",
                   })
# include api_router to main_app
main_app.include_router(api_router)


@main_app.get('/')
async def index():
    return 'hello Kitty'


# connect admin panel to app
admin = create_admin(main_app)

if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
