# Day 311 - Realtime Django WebSocket Project

This project demonstrates **WebSocket integration in Django** using **Django Channels**.  
It allows **real-time communication** between clients and the server, making it suitable for chat apps, live notifications, or real-time dashboards.

---

## Features

- Persistent WebSocket connection between client and server
- Real-time message echo (learning phase)
- Async WebSocket consumer for scalable connections
- Easy to extend for chat rooms, notifications, or dashboards

---

## Tech Stack

- **Backend:** Django 4+, Django Channels
- **Frontend:** Browser WebSocket API (for testing)
- **Protocol:** WebSocket (ws://)
- **ASGI Server:** Daphne (optional for production)
- **Database:** SQLite (default, can be changed)

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd realtime
````

2. Create virtual environment & install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

---

## Run Server

Start Django development server (ASGI ready):

```bash
python manage.py runserver
```

Test WebSocket connection in browser console:

```javascript
const socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onmessage = (e) => console.log(e.data);
socket.onopen = () => socket.send(JSON.stringify({message: "Hello Django"}));
```

Expected response:

```
"You said: Hello Django"
```

---

## Project Structure

```
realtime/
├── chat/
│   ├── consumers.py    # WebSocket logic
│   ├── routing.py      # WebSocket URL routing
│   └── ...
├── realtime/
│   ├── asgi.py         # ASGI entrypoint
│   ├── settings.py     # Django settings
│   └── ...
└── manage.py
```

---


## References

* [Django Channels Documentation](https://channels.readthedocs.io/en/stable/)
* [WebSocket RFC](https://datatracker.ietf.org/doc/html/rfc6455)

---

---