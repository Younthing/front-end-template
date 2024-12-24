from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from ....dependencies import get_token_header

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    email: str

class UserCreate(BaseModel):
    username: str
    email: str

# 模拟数据库
fake_users_db: List[User] = [
    User(id=1, username="johndoe", email="john.doe@example.com"),
    User(id=2, username="alice", email="alice@example.com")
]

@router.get("/", response_model=List[User])
async def read_users():
    """获取所有用户列表"""
    return fake_users_db

@router.post("/", response_model=User)
async def create_user(
    user: UserCreate,
    token: str = Depends(get_token_header)
):
    """创建新用户"""
    new_user = User(
        id=len(fake_users_db) + 1,
        username=user.username,
        email=user.email
    )
    fake_users_db.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    """获取特定用户详情"""
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")