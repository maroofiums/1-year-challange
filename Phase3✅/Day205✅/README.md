

# **Day205 — FastAPI File Uploads & Async Endpoints**

## **📌 Summary**

FastAPI makes file uploads simple using `File` and `UploadFile`. Key points:

* **File**: Upload small files, read into memory.
* **UploadFile**: Async-friendly, ideal for large files.
* **Async endpoints**: Use `async def` to handle multiple requests efficiently.
* **Saving files**: Use `aiofiles` for async writing.
* **Multiple files**: Use `List[UploadFile]`.
* **Always close files** with `await file.close()` to free memory.

---

## **💻 Examples**

### **1️⃣ Single File Upload**

```python
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    size = len(contents)
    await file.close()
    return {"filename": file.filename, "size": size}
```

---

### **2️⃣ Multiple File Uploads**

```python
from typing import List
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    result = []
    for file in files:
        contents = await file.read()
        result.append({"filename": file.filename, "size": len(contents)})
        await file.close()
    return result
```

---

### **3️⃣ Save File to Disk (Async)**

```python
import aiofiles
import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/savefile/")
async def save_file(file: UploadFile = File(...)):
    save_path = f"{UPLOAD_DIR}/{file.filename}"
    async with aiofiles.open(save_path, 'wb') as out_file:
        while content := await file.read(1024):  # read in chunks
            await out_file.write(content)
    await file.close()
    return {"filename": file.filename, "message": "Saved successfully!"}
```

---

### **4️⃣ Async Processing Example**

```python
import asyncio

async def process_file(file: UploadFile):
    await asyncio.sleep(2)  # simulate heavy task
    contents = await file.read()
    await file.close()
    return {"filename": file.filename, "size": len(contents)}

@app.post("/async-upload/")
async def async_upload(file: UploadFile = File(...)):
    result = await process_file(file)
    return result
```

---

## **📝 Mini Project Idea: Async File Processor**

**Goal:**

* Allow users to upload single or multiple files
* Save the files asynchronously
* Run a simple async “processing” task like counting lines or words

**Project Structure:**

```
FastAPI_FileUploads/
│
├── main.py
├── uploads/          # folder to save files
├── requirements.txt
└── README.md
```

**`main.py`** Example:

```python
from fastapi import FastAPI, File, UploadFile
from typing import List
import aiofiles, os, asyncio

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Save files async
async def save_file(file: UploadFile):
    save_path = f"{UPLOAD_DIR}/{file.filename}"
    async with aiofiles.open(save_path, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    await file.close()
    return save_path

# Async process (count lines)
async def process_file(file_path: str):
    async with aiofiles.open(file_path, 'r') as f:
        lines = 0
        async for _ in f:
            lines += 1
    return lines

@app.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        path = await save_file(file)
        line_count = await process_file(path)
        results.append({"filename": file.filename, "lines": line_count})
    return results
```

✅ **What it does:**

1. Uploads files asynchronously
2. Saves them in `uploads/`
3. Processes each file (counting lines) without blocking

---

### **📌 Key Takeaways**

* Use **`UploadFile`** for async uploads.
* Always **close files** after reading.
* Use **aiofiles** to save files without blocking.
* Async endpoints let FastAPI handle **multiple users** efficiently.
* Chunk reading (`await file.read(1024)`) is essential for **large files**.

---

