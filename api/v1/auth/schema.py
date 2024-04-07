from pydantic import BaseModel , EmailStr
from typing import Optional
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id : Optional[int]
    