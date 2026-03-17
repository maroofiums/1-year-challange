# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFaceHub
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("Please set your HF_API_KEY in the .env file")

# Initialize HuggingFace model via LangChain
llm = HuggingFaceHub(
    repo_id="microsoft/DialoGPT-medium",  # Small chat model
    model_kwargs={"temperature": 0.7, "max_new_tokens": 200},
    huggingfacehub_api_token=HF_API_KEY
)

# Initialize conversation memory
memory = ConversationBufferMemory()

# Create LangChain conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
)

# FastAPI app
app = FastAPI(title="LangChain + HuggingFace Chatbot API")

# Enable CORS so Swagger & frontend can call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        reply = conversation.predict(input=req.message)
        return {
            "user_message": req.message,
            "bot_reply": reply
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))