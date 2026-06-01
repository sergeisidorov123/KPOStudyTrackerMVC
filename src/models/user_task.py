from sqlalchemy import ForeignKey, Integer, String
from src.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class UserTask(Base):
    __tablename__ = "user_task"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("task.id"), primary_key=True)
    