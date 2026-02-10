from fastapi import FastAPI
from app.chatbot import ask_bot
from app.schemas import ChatRequest, ChatResponse

app = FastAPI(title="FLAN-T5 Chatbot API")

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    response = ask_bot(req.message)
    return {"response": response}
