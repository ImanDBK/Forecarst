from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    is_active: bool

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool