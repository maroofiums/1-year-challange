from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    artical: str
    
blogs_db = {}

app = FastAPI()

@app.post("/blogs/")
def create_blog(blog: Blog):
    blog_id = len(blogs_db) + 1
    blogs_db[blog_id] = blog
    return {"id":blog_id,"blog":blog}

@app.get("/blogs/")
def get_blog():
    return blogs_db

@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int):
    if blog_id not in blogs_db:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"id": blog_id, "blog": blogs_db[blog_id]}

@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, updated_blog: Blog):
    if blog_id not in blogs_db:
        raise HTTPException(status_code=404, detail="Blog not found")
    blogs_db[blog_id] = updated_blog
    return {"id": blog_id, "blog": updated_blog}

@app.delete("/blogs/{blog_id}")
def delete_item(blog_id: int):
    if blog_id not in blogs_db:
        raise HTTPException(status_code=404, detail="blog not found")
    del blogs_db[blog_id]
    return {"message": f"Item {blog_id} deleted successfully"}