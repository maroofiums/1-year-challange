# ** Day275 - Upload File**

## 🚀 FastAPI Resume Manager (No Database)

A lightweight FastAPI project for uploading resumes (PDF, DOCX, TXT), extracting text, generating simple skill tags, and offering basic CRUD operations — **all without a database**.
Data is stored in memory, making it perfect for beginners, demos, prototypes, or learning FastAPI’s file upload system.

---

## 🌟 Features

✔ Upload PDF / DOCX / TXT resumes
✔ Extract text automatically
✔ Auto-tag using simple keyword matching
✔ List resumes (in-memory)
✔ View resume details
✔ Download uploaded files
✔ Delete resume + file cleanup

---

## 🗂 Project Structure

```
fastapi_no_db/
│
├── main.py        # FastAPI routes + in-memory CRUD
├── utils.py       # File saving + parsing + tagging
└── uploads/       # Saved resumes
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart
pip install pdfplumber
pip install python-docx
```

Or use a single `requirements.txt`:

```
fastapi
uvicorn[standard]
python-multipart
pdfplumber
python-docx
```

Install all:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Start the server:

```bash
uvicorn main:app --reload
```

Open your browser:

**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

You’ll get a clean interactive Swagger UI for testing uploads and CRUD operations.

---

## 📤 Uploading a Resume

**POST** `/resumes/upload`

* UploadFile (`file`)
* Optional `uploaded_by` (name/email/etc.)

Backend will:

1. Save file to `uploads/`
2. Extract text
3. Auto-tag skills
4. Store metadata in memory

---

## 📂 Endpoints Overview

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/resumes/upload`        | Upload + parse resume  |
| GET    | `/resumes`               | List all resumes       |
| GET    | `/resumes/{id}`          | Get single resume      |
| GET    | `/resumes/{id}/download` | Download uploaded file |
| DELETE | `/resumes/{id}`          | Remove resume + file   |

---

## 🎯 Tech Stack

* **FastAPI**
* **Uvicorn**
* **pdfplumber** (PDF parsing)
* **python-docx** (DOCX parsing)
* **Python in-memory storage** (No DB required)

---

## ⚠️ Limitations (Honest & Practical)

* In-memory list → data resets on restart
* Not suitable for production
* Concurrency can overwrite indexes
* Parsing is basic (not ML/NLP optimized)

---