import os
import django
from fastapi import FastAPI
from pydantic import BaseModel

# Django settings configure karo
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Django model import karo
from myapp.models import Item

app = FastAPI(title="FastAPI + Django Example")

class ItemSchema(BaseModel):
    id: int
    name: str
    description: str

@app.get("/items")
def get_items():
    items = Item.objects.all()
    return [ItemSchema(id=item.id, name=item.name, description=item.description) for item in items]

@app.post("/items")
def create_item(item: ItemSchema):
    obj = Item.objects.create(name=item.name, description=item.description)
    return {"id": obj.id, "name": obj.name, "description": obj.description}
