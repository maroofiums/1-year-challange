from fastapi import APIRouter,Path,Query
from app.models import ItemResponse,ItemCreate
from typing import List
route = APIRouter()

items_db: List[ItemCreate] = [
        {
        "name": "Laptop",
        "price": 1200.50,
        "description": "Gaming laptop with RTX GPU",
        "in_stock": True
    },
    {
        "name": "Phone",
        "price": 800.00,
        "description": "Android smartphone",
        "in_stock": True
    },
    {
        "name": "Tablet",
        "price": 450.75,
        "description": "10-inch display tablet",
        "in_stock": False
    }
]

@route.get("/")
def greet():
    return {"msg":"Hello"}

@route.get("/ping")
def pong():
    return {"msg":"pong"}

@route.get("/health")
def healthy():
    return {"msg":"healthy"}

@route.get("/items/",response_model = List[ItemResponse])
def get_items():
    return items_db

@route.post("/items/",response_model = ItemResponse)
def create_items(item:ItemCreate):
    items_db.append(item)   
    return item

@route.get("/items/{item_id}",response_model = ItemResponse)
def get_item(item_id:int):
    return items_db[item_id]

@route.put("/items/{item_id}",response_model = ItemResponse)
def get_item(item_id:int,item:ItemCreate):
    items_db[item_id] = item
    return item

@route.delete("/items/{item_id}")
def get_item(item_id:int):
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item.name}

@route.get("/search")
def search_items(name:str=Query(None)):
    return [
        item for item in items_db
        if name.lower() in item["name"].lower()
    ]