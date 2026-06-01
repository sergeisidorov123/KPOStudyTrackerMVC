from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    name: str
    password: str
    
class UserUpdate(BaseModel):
    username: str
    name: str
    password: str
    group: Optional[str] = None
    
class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    group: Optional[str] = None
    @classmethod
    def from_orm(cls, user):
        return cls(
            id=user.id,
            username=user.username,
            name=user.name,
            group=user.group.name if user.group else None
        )
    
    class Config:
        orm_mode = True