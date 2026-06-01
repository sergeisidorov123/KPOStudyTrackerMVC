from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models import Course 

class CourseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_course(self, name: str, description: str) -> Course:
        new_course = Course(name=name, description=description)
        self.db.add(new_course)
        await self.db.commit()
        await self.db.refresh(new_course)
        return new_course
    
    async def get_course_by_id(self, course_id: int) -> Course | None:
        result = await self.db.execute(
            select(Course).where(Course.id == course_id)
        )
        return result.scalar_one_or_none()

    async def get_all_courses(self) -> list[Course]:
        result = await self.db.execute(select(Course))
        return result.scalars().all()

    async def delete_course(self, course_id: int) -> bool:
        course = await self.get_course_by_id(course_id)
        if course:
            await self.db.delete(course)
            await self.db.commit()
            return True
        return False
        
    async def update_course(self, course_id: int, name: str = None, description: str = None) -> Course | None:
        course = await self.get_course_by_id(course_id)
        if not course:
            return None
        
        if name is not None:
            course.name = name
        if description is not None:
            course.description = description
        
        await self.db.commit()
        await self.db.refresh(course)
        return course
    
    async def assign_course_to_user(self, course_id: int, user_id: int) -> Course | None:
        course = await self.get_course_by_id(course_id)
        if not course:
            return None
        
        course.user_id = user_id
        await self.db.commit()
        await self.db.refresh(course)
        return course