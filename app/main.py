from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import auth
from app.core.database import init_db

app = FastAPI(title="Gmail OAuth API")

@asynccontextmanager
async def lifespan(app: FastAPI): # pylint: disable=unused-argument, redefined-outer-name
    await init_db()
    yield

app = FastAPI(title="Gmail OAuth API", lifespan=lifespan)

app.include_router(auth.router)
