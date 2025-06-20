from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.user import User

async def create_or_update_user(session: AsyncSession, email: str, refresh_token: str):
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalars().one_or_none()

    if user:
        if refresh_token is not None:
            user.refresh_token = refresh_token
            session.add(user)
    else:
        user = User(email=email, refresh_token=refresh_token)
        session.add(user)

    await session.commit()
    await session.refresh(user)
    return user
