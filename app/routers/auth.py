from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from app.core.gmail import get_flow
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.user import create_user
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.config import settings
import httpx
import base64
from app.deps import get_session

router = APIRouter(prefix="/auth", tags=["Google Auth"])

@router.get("/login")
async def login():
    flow = get_flow()
    auth_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(auth_url)

@router.get("/callback")
async def callback(code: str, session: AsyncSession = Depends(get_session)):
    flow = get_flow()
    flow.fetch_token(code=code)

    creds = flow.credentials

    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {creds.token}"}
        res = await client.get("https://gmail.googleapis.com/gmail/v1/users/me/profile", headers=headers)
        profile = res.json()
        print("Gmail profile response:", profile)

    user = await create_user(session, email=profile["emailAddress"], refresh_token=creds.refresh_token)
    return {"message": "User authenticated", "email": user.email}
