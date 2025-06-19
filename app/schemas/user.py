from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    refresh_token: str
