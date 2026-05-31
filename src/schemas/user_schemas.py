from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    name: str
    password: str
    group: str
    
class UserUpdate(BaseModel):
    username: str
    name: str
    password: str
    group: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    group: str
    
    class Config:
        orm_mode = True