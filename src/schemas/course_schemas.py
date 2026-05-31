from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class CourseUpdate(BaseModel):
    name: str
    description: str
    
class CourseResponse(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        orm_mode = True