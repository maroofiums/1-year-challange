from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

class ItemOut(BaseModel):
    name : str
    price: float

router = APIRouter()

items = {}

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.id] = item
    return item

@router.get("/items/", response_model=List[Item])
def read_items():
    return list(items.values())

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    if item_id != updated_item.id:
        raise HTTPException(status_code=400, detail="Item ID cannot be changed")
    items[item_id] = updated_item
    return updated_item

@router.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "Item deleted"}