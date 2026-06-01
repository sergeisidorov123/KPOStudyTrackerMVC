from sqlalchemy import ForeignKey, Integer, String
from src.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class CourseTask(Base):
    __tablename__ = "course_task"
    
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey("course.id"), primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("task.id"), primary_key=True)
    