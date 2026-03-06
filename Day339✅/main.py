from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running on Replit!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}