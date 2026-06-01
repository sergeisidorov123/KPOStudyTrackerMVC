from sqlalchemy.ext.asyncio import AsyncSession
from src.repos.user_repos import UserRepository
from src.models import User, Token
from src.core.security import verify_password, hash_password


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def register_user(self, username: str, password: str, name: str, group: str = None, role: str = "user") -> User:
        if await self.user_repo.get_user_by_username(username):
            raise ValueError("Username already exists")
        password_hash = hash_password(password)
        return await self.user_repo.create_user(username, password_hash, name, group, role)

    async def authenticate_user(self, username: str, password: str) -> User | None:
        user = await self.user_repo.get_user_by_username(username)
        if user and verify_password(password, user.password):
            return user
        return None

    async def create_token_for_user(self, user_id: int, token_str: str) -> Token:
        return await self.user_repo.create_token(user_id, token_str)

    async def invalidate_token(self, token_str: str) -> None:
        await self.user_repo.delete_token(token_str)
        
    async def get_user_courses(self, user_id: int):
        return await self.user_repo.get_user_courses(user_id)
    
    async def get_user_tasks(self, user_id: int):
        return await self.user_repo.get_user_tasks(user_id)
    
    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.user_repo.get_user_by_id(user_id)
    