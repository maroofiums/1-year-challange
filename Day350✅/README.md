# Day 350
# LangChain + HuggingFace Chatbot API

This is a simple **chatbot API** built using **FastAPI** and **LangChain**, powered by a **HuggingFace model**.  
The chatbot supports **conversation memory**, so it remembers previous messages in the session.

---

## Features

- FastAPI backend for chat
- HuggingFace model integration via LangChain
- Conversation memory with `ConversationBufferMemory`
- CORS enabled for browser/front-end requests
- Easy to switch models
- Error handling for safe API calls

---

## Requirements

- Python 3.10+
- HuggingFace API token
- Packages listed in `requirements.txt`:

```text
fastapi
uvicorn
langchain
transformers
python-dotenv
huggingface_hub
````

---

## Setup

1. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
# OR
source venv/bin/activate       # Linux/Mac
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your HuggingFace API key:

```text
HF_API_KEY=your_huggingface_api_key
```

---

## Running the API

```bash
uvicorn main:app --reload
```

* Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Usage

### Endpoint

**POST** `/chat`

**Request Body:**

```json
{
  "message": "Hi there!"
}
```

**Response:**

```json
{
  "user_message": "Hi there!",
  "bot_reply": "Hello! How can I help you today?"
}
```

---

## Notes

* **Conversation Memory:** The bot will remember previous messages in the current session.
* **CORS:** Enabled for all origins (`*`) for testing. In production, replace with your frontend URL.
* **Model:** Default model is `microsoft/DialoGPT-medium`. You can replace it with other HuggingFace models.
* **Error Handling:** API safely returns errors instead of crashing.

---
