# fastapi_app/router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "FastAPI is working with Django!"}

@router.get("/hello")
def say_hello():
    return {"greet": "Hello from FastAPI!"}
