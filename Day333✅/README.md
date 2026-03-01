# Day333 - URL Shortener (Streamlit + FastAPI + TinyURL)

A simple URL shortener app with **Streamlit frontend** and **FastAPI backend**, using the **TinyURL API** for shortening URLs.  
No database is required — fully API-based.

---

## Live Demo

Check out the live app: [https://url-shortnr.streamlit.app/](https://url-shortnr.streamlit.app/)

---

## Repository Structure

```

URL-Shortener/
├── UI
│   └── main.py        # Streamlit frontend
├── app
│   └── main.py        # FastAPI backend
└── README.md

````

---

## Features

- Shorten URLs instantly via TinyURL API
- Streamlit frontend for easy user interaction
- FastAPI backend handles URL shortening
- No database required
- Configurable backend URL via `.env`

---

## Tech Stack

- **Frontend:** Streamlit (`UI/main.py`)
- **Backend:** FastAPI (`app/main.py`)
- **URL Shortening:** TinyURL API
- **Environment Variables:** `python-dotenv`

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/maroofiums/URL-Shortener.git
cd URL-Shortener
````

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your backend URL:

```env
BACKEND_URL=http://127.0.0.1:8000/shorten
```

---

## Running the Project

### 1. Start FastAPI backend

```bash
uvicorn app.main:app --reload
```

The backend will be available at `http://127.0.0.1:8000`.

### 2. Start Streamlit frontend

```bash
streamlit run UI/main.py
```

Open the Streamlit URL shown in the terminal to use the app.

---

## Usage

1. Enter the URL you want to shorten.
2. Click **Shorten URL**.
3. The app will display the original URL and the shortened TinyURL.
4. Click the link to open the shortened URL.

---

## Notes

* No database is used; shortening relies on TinyURL API.
* You can switch backend URL by updating the `.env` file.
* App resets if the backend server stops (since no database).

---

## Dependencies

* `fastapi`
* `uvicorn`
* `requests`
* `streamlit`
* `python-dotenv`
* `pydantic`

---
