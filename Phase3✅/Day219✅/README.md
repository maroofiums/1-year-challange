# Day 219 - **File Analyzer Web App**

A simple **FastAPI** project to upload files (CSV, text, images) and get a **quick analysis / preview**. Great for learning file handling, FastAPI endpoints, and basic data/image processing.

---

## **Features**

* Upload **CSV files** → View first 5 rows, columns, and total rows
* Upload **Text files** → Preview first 200 characters and word count
* Upload **Images (jpg/png)** → View dimensions, format, and size
* **Optional:** Save uploaded files on the server
* Fully **async-friendly** using FastAPI’s `UploadFile`

---

## **Tech Stack**

* **Backend:** FastAPI
* **Libraries:** Pandas (CSV), Pillow (Images), python-multipart (File uploads)
* **Server:** Uvicorn
* **Optional Frontend:** Simple HTML form / Swagger UI

---

## **Installation**

1. **Clone the repo:**

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## **Run the app**

```bash
uvicorn main:app --reload
```

Open your browser at:

```
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to upload files and see previews.

---

## **Usage Examples**

* **CSV:** Upload `data.csv` → Returns columns, row count, and first 5 rows
* **Text:** Upload `notes.txt` → Returns first 200 characters and file length
* **Image:** Upload `photo.jpg` → Returns image size, format, and type

---

## **Project Structure**

```
FileAnalyzer/
│
├── main.py          # FastAPI backend
├── requirements.txt # Python dependencies
├── files/           # Optional folder to save uploaded files
└── README.md
```

---

## **Future Enhancements**

* Add **file type validation**
* Save uploaded files permanently with timestamp
* Add **frontend UI** with preview & download
* Add **CSV/Excel plotting** for data visualization

---

💡 **Tip:** This project is small but covers **real-world file handling, async endpoints, and integration with pandas/pillow** — perfect for learning and portfolio.

---

