from fastapi import FastAPI, Depends
import uvicorn
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import db_config, Product
from api import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_config.dispose()


main_app = FastAPI(lifespan=lifespan, title='Sneakers shop',
                   description="prjct for learn FastAPI",
                   version='0.0.1',
                   contact={
                       "name": "Ivan Levchuk",
                       "email": "swankyyy1@gmail.com",
                   })
main_app.include_router(api_router)


@main_app.get('/')
async def index():
    return 'hello Kitty'


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
