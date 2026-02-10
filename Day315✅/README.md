# Day 315 - FLAN-T5 FastAPI Chatbot

A lightweight FastAPI-based chatbot using HuggingFace's **FLAN-T5** model via **transformers pipeline**.  
This setup works fully on free-tier and avoids LangChain HFEndpoint issues.

---

## Features

- Uses **google/flan-t5-base** (text2text seq2seq model)
- FastAPI REST API for chat
- Safe free-tier usage (no paid models required)
- Easy to extend with streaming or memory

---

## Project Structure

```

.
├── app/
│   ├── chatbot.py      # FLAN-T5 pipeline + ask_bot function
│   ├── main.py         # FastAPI app
│   ├── schemas.py      # Pydantic request/response models
│   └── test.py         # Standalone test script
├── .env                # Model configuration
├── requirements.txt    # Python dependencies
└── README.md

```

---

## Setup

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Configure .env**

```env
MODEL_NAME=google/flan-t5-base
```

---

## Run Chatbot (Standalone)

```bash
python -m app.test
```

Example:

```python
from app.chatbot import ask_bot

print(ask_bot("Explain FastAPI in one line"))
```

Output:

```
FastAPI is a fast Python framework for building APIs with automatic validation.
```

---

## Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

* Open Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Test the `/chat` POST endpoint:

```json
{
  "message": "Hi, explain FastAPI"
}
```

Response:

```json
{
  "response": "FastAPI is a fast Python framework for building APIs with automatic validation."
}
```

---

## Notes

* FLAN-T5 = seq2seq → requires `text2text-generation`
* Using LangChain HFEndpoint with FLAN-T5 free-tier may fail → transformers pipeline is recommended
* Max tokens in pipeline = 128 (adjustable)
* Fully compatible with **Windows, Linux, Mac**

---
