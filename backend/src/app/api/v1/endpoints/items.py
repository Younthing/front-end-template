from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

# 模拟数据库
fake_items_db = []

@router.get("/", response_model=List[Item])
async def read_items():
    """获取所有物品列表"""
    return fake_items_db

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    """创建新物品"""
    new_item = Item(
        id=len(fake_items_db) + 1,
        name=item.name,
        description=item.description,
        price=item.price
    )
    fake_items_db.append(new_item)
    return new_item