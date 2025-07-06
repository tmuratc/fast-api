from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db
from app.routes import clans
from fastapi import Request
from fastapi.responses import JSONResponse
#from dotenv import load_dotenv


#load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield  # cleanup yapılacaksa buraya yazılır

app = FastAPI(lifespan=lifespan)

app.include_router(clans.router)


@app.middleware("http")
async def limit_body_size(request: Request, call_next):
    max_body_size = 10 * 1024  # 10 KB
    body = await request.body()
    if len(body) > max_body_size:
        return JSONResponse(content={"detail": "Payload too large"}, status_code=413)
    request._body = body
    return await call_next(request)
