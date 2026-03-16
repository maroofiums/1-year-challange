# Day349 - FastAPI Item Management API

A simple **FastAPI project** demonstrating CRUD operations, search functionality, and the use of **Pydantic models** as a fake database. This project is suitable for learning **FastAPI fundamentals** and building small backend APIs.

---

## Project Structure

```

project/
├── app
│   ├── **init**.py
│   ├── models.py        # Pydantic models (ItemCreate, ItemResponse)
│   └── routes.py        # API routes (CRUD + search)
├── main.py              # FastAPI app entrypoint
└── README.md

````

---

## Features

- **CRUD operations**
  - Create new items
  - Read all items or single item by index
  - Update items
  - Delete items
- **Search functionality**
  - Search items by name (case-insensitive)
- **Response models**
  - Use `ItemResponse` to control what fields are returned
- **Fake database**
  - List of Pydantic objects (`items_db`) simulates a database
- **FastAPI automatic docs**
  - OpenAPI documentation available at `/docs` and `/redoc`

---

## Installation


1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## Run the Project

```bash
uvicorn main:app --reload
```

* The server will run on `http://127.0.0.1:8000`
* Open API docs at `http://127.0.0.1:8000/docs`
* Redoc docs at `http://127.0.0.1:8000/redoc`

---

## Example Endpoints

| Method | Endpoint           | Description                        |
| ------ | ------------------ | ---------------------------------- |
| GET    | `/items/`          | Get all items                      |
| POST   | `/items/`          | Create a new item                  |
| GET    | `/items/{item_id}` | Get single item by index           |
| PUT    | `/items/{item_id}` | Update item by index               |
| DELETE | `/items/{item_id}` | Delete item by index               |
| GET    | `/search?name=xxx` | Search items by name (query param) |

---

## Example Request & Response

**POST /items/**

Request body:

```json
{
  "name": "Laptop",
  "price": 1200.50,
  "description": "Gaming laptop with RTX GPU",
  "in_stock": true
}
```

Response:

```json
{
  "name": "Laptop",
  "price": 1200.50
}
```

---

## Notes

* This project uses **in-memory storage** (list of Pydantic models). Data will reset when the server restarts.
* For production, integrate with a **database** (SQLite, PostgreSQL, MongoDB, etc.)
* Search is **case-insensitive** and works on the `name` field.
* Use `ItemCreate` for **input** and `ItemResponse` for **output** to control returned fields.
