# fastapi_app/main.py
from fastapi import FastAPI
from fastapi_app import router  # Make sure this is correct

app = FastAPI()

app.include_router(router.router)  # Use correct path to your router
