from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="FastAPI Backend",
    version="1.0.0"
)

app.include_router(health_router)

@app.get("/")
def root():
    return {"status": "Backend is running"}
