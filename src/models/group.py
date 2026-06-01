from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship, Mapped   
from src.core.database import Base

class Group(Base):
    __tablename__ = "group"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    
    course = relationship("Course", back_populates="group")
    user = relationship("User", back_populates="group")