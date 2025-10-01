from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Dockerized FastAPI 🚀"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hey {name}, welcome to FastAPI in Docker!"}
