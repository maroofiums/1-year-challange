from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
from typing import List
from utils import save_upload_file, extract_text_auto, simple_tag_extraction

app = FastAPI()

RESUMES = []
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...),
    uploaded_by: str | None = None
):
    # ---- FIX 1: Force filename to be string always ----
    filename = str(file.filename)

    if not filename:
        raise HTTPException(status_code=400, detail="Invalid file name")

    # Extract extension safely
    filename = os.path.basename(filename)
    base, extname = os.path.splitext(filename)

    ext_lower = extname.lower()

    allowed = {".pdf", ".docx", ".txt"}
    if ext_lower not in allowed:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # ---- FIX 2: Prepare save path & handle duplicate names ----
    save_path = os.path.join(UPLOAD_DIR, filename)

    counter = 1
    while os.path.exists(save_path):
        filename = f"{base}_{counter}{extname}"
        save_path = os.path.join(UPLOAD_DIR, filename)
        counter += 1

    # ---- FIX 3: Save file safely ----
    await save_upload_file(file, save_path)

    # ---- FIX 4: Extract resume content ----
    text = extract_text_auto(save_path)
    tags = simple_tag_extraction(text)

    resume_obj = {
        "id": len(RESUMES) + 1,
        "filename": filename,
        "file_path": save_path,
        "uploaded_by": uploaded_by,
        "tags": tags,
        "content_preview": text[:200]
    }

    RESUMES.append(resume_obj)
    return resume_obj


@app.get("/resumes")
def list_resumes() -> List[dict]:
    return RESUMES


@app.get("/resumes/{resume_id}")
def get_resume(resume_id: int):
    for r in RESUMES:
        if r["id"] == resume_id:
            return r
    raise HTTPException(status_code=404, detail="Resume not found")


@app.delete("/resumes/{resume_id}")
def delete_resume(resume_id: int):
    global RESUMES

    for r in RESUMES:
        if r["id"] == resume_id:
            try:
                if os.path.exists(r["file_path"]):
                    os.remove(r["file_path"])
            except:
                pass

            RESUMES = [x for x in RESUMES if x["id"] != resume_id]
            return {"detail": "deleted"}

    raise HTTPException(status_code=404, detail="Resume not found")


@app.get("/resumes/{resume_id}/download")
def download(resume_id: int):
    for r in RESUMES:
        if r["id"] == resume_id:
            return FileResponse(r["file_path"], filename=r["filename"])

    raise HTTPException(status_code=404, detail="Resume not found")
