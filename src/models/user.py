from sqlalchemy import Integer, String, Enum, ForeignKey
from src.core.database import Base
import enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

class UserEnum(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    username: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
    role: Mapped[UserEnum] = mapped_column(Enum(UserEnum), default=UserEnum.USER)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("group.id"), nullable=True)
    
    
    courses = relationship("Course", secondary="user_course", back_populates="users")
    tasks = relationship("Task", secondary="user_task", back_populates="user")
    group = relationship("Group", back_populates="user")
    tokens = relationship("Token", back_populates="user")