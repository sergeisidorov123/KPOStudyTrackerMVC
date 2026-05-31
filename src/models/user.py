from sqlalchemy import Integer, String, Enum
from src.core.database import Base
import enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

class User(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(150), nullable=False)
    group: Mapped[str] = mapped_column(String(150), nullable=True)
    role: Mapped[User] = mapped_column(Enum(User), default=User.USER)
    
    courses = relationship("Course", back_populates="user")
    tasks = relationship("Task", back_populates="user")
    group = relationship("Group", back_populates="user")
    token = relationship("Token", back_populates="user")