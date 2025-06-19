from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth
from app.core.database import init_db

app = FastAPI(title="Gmail OAuth API")

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(auth.router)
