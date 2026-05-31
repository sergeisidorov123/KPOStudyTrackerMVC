from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
    deadline: str
    course_id: int
    
class TaskUpdate(BaseModel):
    title: str
    description: str
    deadline: str
    status: str
    
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    deadline: str
    status: str
    
    class Config:
        orm_mode = True