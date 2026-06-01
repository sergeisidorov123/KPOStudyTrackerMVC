from src.models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Token

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_username(self, username: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def create_user(self, username: str, password_hash: str, group: str = None, role: str = "user") -> User:
        new_user = User(username=username, password_hash=password_hash, group=group, role=role)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def get_user_by_id(self, user_id: int) -> User | None:
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all_users(self) -> list[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all()
    
    async def delete_user(self, user_id: int) -> bool:
        user = await self.get_user_by_id(user_id)
        if user:
            await self.db.delete(user)
            await self.db.commit()
            return True
        return False
    
    async def update_user(self, user_id: int, username: str = None, password_hash: str = None, group: str = None, role: str = None) -> User | None:
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        
        if username is not None:
            user.username = username
        if password_hash is not None:
            user.password_hash = password_hash
        if group is not None:
            user.group = group
        if role is not None:
            user.role = role
        
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def create_token(self, user_id: int, token_str: str) -> Token:
        new_token = Token(token=token_str, user_id=user_id)
        self.db.add(new_token)
        await self.db.commit()
        await self.db.refresh(new_token)
        return new_token
    
    async def get_user_by_token(self, token_str: str) -> User | None:
        result = await self.db.execute(
            select(Token).where(Token.token == token_str)
        )
        token = result.scalar_one_or_none()
        if token:
            return token.user
        return None
    
    async def delete_token(self, token_str: str) -> bool:
        result = await self.db.execute(
            select(Token).where(Token.token == token_str)
        )
        token = result.scalar_one_or_none()
        if token:
            await self.db.delete(token)
            await self.db.commit()
            return True
        return False
    
    