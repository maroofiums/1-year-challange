from app.routes import route
from fastapi import FastAPI

app = FastAPI()

app.include_router(route)
