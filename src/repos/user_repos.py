from sqlalchemy.orm import Session
from src.models import User
from src.models import Group
from src.models import Token

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, username: str, password_hash: str, group: str = None, role: str = "user") -> User:
        new_user = User(username=username, password_hash=password_hash, group=group, role=role)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_all_users(self) -> list[User]:
        return self.db.query(User).all()
    
    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
    
    def update_user(self, user_id: int, username: str = None, password_hash: str = None, group: str = None, role: str = None) -> User | None:
        user = self.get_user_by_id(user_id)
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
        
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def create_token(self, user_id: int, token_str: str) -> Token:
        new_token = Token(token=token_str, user_id=user_id)
        self.db.add(new_token)
        self.db.commit()
        self.db.refresh(new_token)
        return new_token
    
    def get_user_by_token(self, token_str: str) -> User | None:
        token = self.db.query(Token).filter(Token.token == token_str).first()
        if token:
            return token.user
        return None
    
    def delete_token(self, token_str: str) -> bool:
        token = self.db.query(Token).filter(Token.token == token_str).first()
        if token:
            self.db.delete(token)
            self.db.commit()
            return True
        return False
    
    