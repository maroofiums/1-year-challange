from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/chat")
async def chat(message: str):
    if not message:
        return {"error": "Message cannot be empty"}
    elif "name" in message.lower():
        return {"response": "Hello! How can I assist you today?"}

    elif "help" in message.lower():
        return {"response": "Sure! What do you need help with?"}

    elif "hello" in message.lower():
        return {"response": "Hi there! How can I help you?"}
    
    elif "bye" in message.lower():
        return {"response": "Goodbye! Have a great day!"}
    
    else:
        return {"response": "I'm not sure how to respond to that. Can you please clarify?"}
    
    return {"response": "This is a default response."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
