from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # cleanup yapılacaksa buraya yazılır

app = FastAPI(lifespan=lifespan)
