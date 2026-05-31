from sqlalchemy import Enum, Integer, String
from src.core.database import Base
import enum
from sqlalchemy.orm import relationship, Mapped, mapped_column


class TaskStatus(enum.Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    
class Task(Base):
    __tablename__ = "task"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    course = relationship("Course", back_populates="tasks")
    deadline: Mapped[str] = mapped_column(String(50), nullable=True)
    status = mapped_column(Enum(TaskStatus), default=TaskStatus.TO_DO)
    