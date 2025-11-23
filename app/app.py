from fastapi import FastAPI, HTTPException
from app.schema import PostCreate, PostResponse
from app.db import create_db_and_tables, get_async_session

from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)