from fastapi import FastAPI, Depends
import uvicorn

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_config, Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_config.dispose()


main_app = FastAPI(lifespan=lifespan)


@main_app.get('/')
async def index():

    return 'hello Kitty'


if __name__ == "__main__":
    uvicorn.run("main:main_app", reload=True)
