# Day233 -- 🚀 FastAPI File Uploads & Async Endpoints

Yeh project FastAPI ka simple aur clean example hai jisme:

* **Async endpoints**
* **CRUD operations** (items list ke liye)
* **File upload endpoint**
* **Pydantic models**
* **In-memory list storage**

Sab kuch beginner-friendly structure mein.

---

## 📦 **Features**

* Fully **async** API → fast & scalable
* CRUD system using pure Python list
* Upload any file (`UploadFile`)
* Automatic validation via Pydantic
* Response models → clean & consistent API structure

---

## 📁 **Project Structure**

```
project/
│── main.py          # FastAPI application
│── requirements.txt # Dependencies
```

---

## 🔧 **Installation & Setup**

### 1. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 2. Install FastAPI + Uvicorn

```bash
pip install fastapi uvicorn
```

---

## ▶️ **Run the Server**

```bash
uvicorn main:app --reload
```

* `--reload` → hot reload
* App auto-starts on → **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
* Interactive Docs → **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

# 🧠 **Async CRUD Example (Simple Items API)**

### **GET all Items**

```
GET /items/
```

### **GET single Item**

```
GET /item/{item_id}
```

### **POST create new Item**

```
POST /item/
```

Body Example:

```json
{
  "name": "Laptop",
  "price": 1500,
  "is_stock": true
}
```

### **PUT update existing Item**

```
PUT /items/{item_id}
```

### **DELETE Item**

```
DELETE /items/{item_id}
```

---

# 📁 **File Upload Endpoint**

FastAPI provides `UploadFile` for async file uploads — bohot fast & memory-efficient.

### **Endpoint**

```
POST /upload-file/
```

### **Example Endpoint Code**

```python
from fastapi import UploadFile, File

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    size = len(content)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": size,
        "message": "File uploaded successfully"
    }
```

---

# 📤 **How to Upload a File (Swagger UI)**

1. Visit:
   **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

2. Select → `POST /upload-file/`

3. Click: **"Choose File"**

4. Upload any file

5. Hit **Execute**

---

# 📌 Notes & Best Practices

* Async endpoints recommended for:

  * file uploads
  * database operations
  * network calls
* `UploadFile` is better than `bytes` because:

  * doesn’t load entire file in memory
  * supports streaming
* For saving files → use `aiofiles` (async file writing)

Example save-to-disk snippet:

```python
import aiofiles

@app.post("/save-file/")
async def save_file(file: UploadFile = File(...)):
    async with aiofiles.open(f"uploads/{file.filename}", "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
    return {"message": "File saved"}
```

---

# 📝 **Summary**

Ye project tumhein FastAPI ke 2 important concepts sikhata hai:

1. **Async API development** → fast & scalable
2. **File Upload Handling** → UploadFile + async read
