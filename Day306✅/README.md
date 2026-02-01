# Day 306 - Chat-Style AI with Hugging Face + LangChain

A simple **chatbot** built using **Hugging Face transformers** and **LangChain** in Python.  
This project demonstrates how to create a **local AI assistant** that can answer questions, tell jokes, or have multi-turn conversations.

---

## 🔹 Features

- Chat-style AI using `.invoke()` method  
- Powered by Hugging Face models (e.g., GPT-2)  
- Easy to extend with **memory** or **additional tools**  
- Works **locally** on CPU for small models  

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/maroof2424/langchain-hf-chatbot.git
cd langchain-hf-chatbot
````

2. Install dependencies:

```bash
pip install --upgrade langchain-huggingface transformers torch
```

---

## ⚡ Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import ChatHuggingFace

# Load tokenizer & model
model_id = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Create pipeline
chat_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=0.7
)

# Wrap in chat LLM
chat_llm = ChatHuggingFace(llm=chat_pipe)

# Chat!
print(chat_llm.invoke("Hello! Tell me a joke about a robot and a cat."))
```

---

## 📌 How It Works

1. **Hugging Face pipeline** loads the pre-trained model for text generation.
2. **ChatHuggingFace** wraps the pipeline so it can be used like a chatbot.
3. `.invoke("your prompt")` generates a reply in **chat style**.

---
