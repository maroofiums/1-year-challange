from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteBase(BaseModel):
    title: str
    content: str
    tag: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tag: Optional[str] = None

class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
