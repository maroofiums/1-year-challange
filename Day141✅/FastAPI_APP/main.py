from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Pydantic Model

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


# Helpers (Save/Load JSON)

def load_data(file="data.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data, file="data.json"):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Routes


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

@app.get("/items/")
def get_items():
    data = load_data()
    return {"items": data}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    data = load_data()
    if 0 <= item_id < len(data):
        return {"item": data[item_id], "query": q}
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(item: Item):
    data = load_data()
    data.append(item.dict())
    save_data(data)
    return {"message": "Item created", "item": item.dict()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    data = load_data()
    if 0 <= item_id < len(data):
        data[item_id] = item.dict()
        save_data(data)
        return {"message": "Item updated", "item": data[item_id]}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    data = load_data()
    if 0 <= item_id < len(data):
        deleted_item = data.pop(item_id)
        save_data(data)
        return {"message": f"Item {item_id} deleted", "deleted": deleted_item}
    return {"error": "Item not found"}
