# asgi.py (root level)
import os
import django
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.asgi import get_asgi_application
from fastapi_app.router import router as fastapi_router

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

app = FastAPI()

# Mount Django
app.mount("/django", WSGIMiddleware(get_asgi_application()))

# Mount FastAPI
app.include_router(fastapi_router, prefix="/api")
