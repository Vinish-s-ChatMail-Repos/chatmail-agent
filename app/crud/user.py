from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.user import User

async def create_user(session: AsyncSession, email: str, refresh_token: str):
    user = User(email=email, refresh_token=refresh_token)
    session.add(user)
    await session.commit()
    return user
