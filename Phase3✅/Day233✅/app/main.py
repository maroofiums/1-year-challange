from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field

app = FastAPI()

items = []

class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    is_stock: bool = False

class ItemOut(BaseModel):
    id: int
    name: str
    price: float = Field(..., gt=0)
    is_stock: bool = False


@app.get("/items/", response_model=list[ItemOut])
async def read_items():
    return items


@app.get("/item/{item_id}", response_model=ItemOut)
async def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not Found")


@app.post("/item/", response_model=ItemOut)
async def create_item(item: Item):
    new_id = len(items) + 1
    new_item = {"id": new_id, **item.dict()}
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}", response_model=ItemOut)
async def update_item(item_id: int, update_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = {"id": item_id, **update_item.dict()}
            return items[index]
    raise HTTPException(status_code=404, detail="Item not Found")


@app.delete("/items/{item_id}", response_model=ItemOut)
async def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted = items.pop(index)
            return deleted
    raise HTTPException(status_code=404, detail="Item not Found")


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()  # async I/O
    file_size = len(content)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": file_size,
        "message": "File uploaded successfully"
    }
