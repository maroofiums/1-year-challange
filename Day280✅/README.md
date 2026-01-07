## 🎯 Day280

> **A working chatbot system** jahan
> Django = frontend + user
> FastAPI = chatbot brain (API)

End of day tum dikha sako:
✔ Chat UI
✔ API call
✔ Bot response

---

## 🧠 Step 1: Architecture (dimagh mein picture banao)

```
User (Browser)
   ↓
Django (UI + form)
   ↓ API call
FastAPI (Chatbot logic)
   ↓ response
Django → User
```

👉 **Django smart frontend**
👉 **FastAPI fast brain**

Best combo 💯

---

## 🧩 Step 2: Decide chatbot level (honest advice)

❌ LLM
❌ Heavy ML
❌ Training models

✅ Rule-based / intent-based chatbot

Reason:

> Project ka goal = **integration + flow**, not AI research

---

## 🛠️ Step 3: FastAPI – Chatbot API (Brain)

### `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    user_msg = msg.text.lower()

    if "hello" in user_msg:
        reply = "Hi! How can I help you?"
    elif "name" in user_msg:
        reply = "I am your AI assistant 🤖"
    elif "bye" in user_msg:
        reply = "Goodbye! Take care 👋"
    else:
        reply = "Sorry, I didn't understand that."

    return {"reply": reply}
```

👉 Simple
👉 Explainable
👉 Extendable later

---

## 🧠 Step 4: Django – Simple Chat UI

### `views.py`

```python
import requests
from django.shortcuts import render

def chat_view(request):
    response = None

    if request.method == "POST":
        user_text = request.POST.get("message")

        api_response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"text": user_text}
        )

        response = api_response.json()["reply"]

    return render(request, "chat.html", {"response": response})
```

---

### `chat.html`

```html
<form method="post">
  {% csrf_token %}
  <input type="text" name="message" placeholder="Say something..." required>
  <button type="submit">Send</button>
</form>

{% if response %}
  <p><b>Bot:</b> {{ response }}</p>
{% endif %}
```

🔥 Chat working end-to-end

---

## 🧪 Step 5: Test Flow (important)

1. Run FastAPI → `uvicorn main:app`
2. Run Django → `python manage.py runserver`
3. Open browser
4. Type: **hello**
5. Bot replies 🎉

Agar yeh kaam kar gaya →
**Saturday successful** ✅

---

## ❌ Common Mistakes (avoid karo)

* ❌ Django + FastAPI ek hi app banana
* ❌ AI model direct add karna
* ❌ Perfect UI pe time waste

---

## ✅ Best Practices (mentor advice)

✔ Services separate rakho
✔ API stateless rakho
✔ Simple chatbot logic pehle
✔ README likhna mat bhoolna

---

## 🧠 How to explain this project (interview line)

> “I built a modular chatbot system where Django handles the frontend and FastAPI serves an AI-powered backend via REST APIs.”

🔥 Clean + professional

---

## 🧠 Short Summary

* Django = user interface
* FastAPI = chatbot logic
* API = bridge
* Simple AI = smart project