from fastapi import Depends
from app.core.database import async_session
from sqlmodel.ext.asyncio.session import AsyncSession

from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
