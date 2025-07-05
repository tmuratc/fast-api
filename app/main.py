from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.routes import clans

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # cleanup yapılacaksa buraya yazılır

app = FastAPI(lifespan=lifespan)

app.include_router(clans.router)

