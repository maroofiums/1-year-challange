from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="URL Shortener API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class URLRequest(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(data: URLRequest):
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={data.url}")
        if response.status_code == 200:
            return {"original_url": data.url, "short_url": response.text}
        else:
            raise HTTPException(status_code=400, detail="Failed to shorten URL")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))