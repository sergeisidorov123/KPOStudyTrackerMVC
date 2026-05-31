from pydantic import BaseModel

class GroupCreate(BaseModel):
    name: str
    description: str
    
class GroupUpdate(BaseModel):
    name: str
    description: str

class GroupResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        orm_mode = True