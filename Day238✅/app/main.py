from fastapi import FastAPI
from app.routes import router as predict_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ML Model API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict_router)

@app.get("/")
def root():
    return {"message":"Wellcome to ML Model API!..."}