
# Day285 -- Notes Manager

A simple and modern Notes Manager web application built with **FastAPI** (backend) and **Next.js** (frontend) using **TailwindCSS**.  

Users can **create, read, update, and delete notes** with optional tags. The app is lightweight, beginner-friendly, and serves as a real-world full-stack project.

---

## Features

- Add, edit, and delete notes
- Optional tags for notes
- FastAPI backend with SQLite database
- Next.js 13 frontend with TailwindCSS (CDN)
- Responsive UI for desktop and mobile

---

## Tech Stack

- **Backend:** FastAPI, SQLAlchemy, SQLite  
- **Frontend:** Next.js 13 (app directory), React, TailwindCSS (via CDN)  
- **Middleware:** CORS  
- **Dev Tools:** Uvicorn, Node.js, npm  

---

## Project Structure

### Backend (`Backend/app`)
```

app/
├── main.py           # FastAPI entrypoint
├── routes.py         # API routes for notes
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── database.py       # Database connection and session

```

### Frontend (`notes-frontend/app`)
```

app/
├── layout.js         # Root layout with Tailwind CDN
├── page.js           # Home page (list + add notes)
├── edit/[id]/page.js # Edit note page
├── components/
│   ├── NoteForm.js   # Form to add/edit note
│   └── NotesList.js  # List of notes

````

---

## Installation & Setup

### Backend

1. Go to backend folder:

```bash
cd Backend
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

4. Run the backend server:

```bash
uvicorn app.main:app --reload
```

* Backend runs on [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Check `/notes` endpoint with Postman or browser

---

### Frontend

1. Go to frontend folder:

```bash
cd notes-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend dev server:

```bash
npx next dev
```

* Frontend runs on [http://localhost:3000](http://localhost:3000)
* TailwindCSS is included via CDN

---

## Usage

1. Open [http://localhost:3000](http://localhost:3000)
2. Add a new note using the form
3. View all notes in the list below
4. Delete a note using the **Delete** button
5. Edit a note (if edit page implemented)

---

## Notes

* Backend uses **SQLite** for simplicity. For production, consider PostgreSQL or MySQL
* TailwindCSS is used via **CDN** to avoid build issues on Windows + Next.js 16 + Turbopack
* For production deployment, switch to a local Tailwind setup

---
