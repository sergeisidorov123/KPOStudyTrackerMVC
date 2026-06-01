from sqlalchemy import ForeignKey, Integer, String
from src.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

class Course(Base):
    __tablename__ = "course"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("group.id"), nullable=True)
    
    
    users = relationship("User", secondary="user_course", back_populates="courses")
    group = relationship("Group", back_populates="course")
    tasks = relationship("Task", back_populates="course")
    