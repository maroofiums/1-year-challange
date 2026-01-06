from fastapi import FastAPI,UploadFile,File
from PIL import Image
import pandas as pd
import io

app = FastAPI()

@app.post("/uploadfile/")
def read_file(file:UploadFile=File(...)):
    info = {"filename":file.filename,"content_type":file.content_type}
    if file.filename.lower().endswith(".csv"):
        df = pd.read_csv(file.file)
        info.update({
            "columns":df.columns.tolist(),
            "rows": len(df),
            "preview": df.head().to_dict()
        })
    if file.filename.lower().endswith(".txt"):
        content = file.read()
        text = content.decode("utf-8")

        info.update({
            "lenght": len(text),
            "preview": text[:200]
        })
    elif file.filename.lower().endswith((".png",".jpg",".jpeg")):
        image = Image.open(file.file)
        info.update({
            "size": image.size,
            "format": image.format,
        })
    return info