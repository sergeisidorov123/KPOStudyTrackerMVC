from sqlalchemy import Integer, String, mapped_column
from src.core.database import Base
from sqlalchemy.orm import relationship, Mapped

class Course(Base):
    __tablename__ = "course"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    
    
    user = relationship("User", back_populates="courses")