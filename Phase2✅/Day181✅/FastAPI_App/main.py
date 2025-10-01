from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello Fastapi"}

@app.get("/ping")
def ping():
    return {"pong":True}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Combined Django + FastAPI Docs",
        version="1.0.0",
        description="This docs includes both Django & FastAPI routes",
        routes=app.routes,
    )
    openapi_schema["paths"]["/api/books/"] = {
        "get": {
            "summary": "List Books (from Django)",
            "responses": {"200": {"description": "A list of books"}},
        }
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi