from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.schemas.user_schemas import UserCreate,UserUpdate, UserResponse
from src.schemas.auth_schemas import *
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
http_bearer = HTTPBearer()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        user_service = UserService(db)
        new_user = await user_service.register_user(user.username, user.password, user.name)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user