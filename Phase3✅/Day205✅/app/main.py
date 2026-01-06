from fastapi import FastAPI, File, UploadFile
from typing import List
import aiofiles
import asyncio
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Multiple files
@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    result = []
    for file in files:
        contents = await file.read()
        result.append({"filename": file.filename, "size": len(contents)})
        await file.close()
    return result

# Save file to disk
@app.post("/savefile/")
async def save_file(file: UploadFile = File(...)):
    save_path = f"{UPLOAD_DIR}/{file.filename}"
    
    async with aiofiles.open(save_path, 'wb') as out_file:
        while content := await file.read(1024): 
            await out_file.write(content)
    
    await file.close()
    return {"filename": file.filename, "message": "Saved successfully!"}

# Async processing
async def process_file(file: UploadFile):
    await asyncio.sleep(2)  # simulate heavy task
    contents = await file.read()
    await file.close()
    return {"filename": file.filename, "size": len(contents)}

@app.post("/async-upload/")
async def async_upload(file: UploadFile = File(...)):
    result = await process_file(file)
    return result
