from fastapi import APIRouter, Depends, Query,Path,HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import schemas,models
from database import get_db

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/", response_model=List[schemas.NoteResponse])
def get_notes(db:Session=Depends(get_db),
              skip:int=0,
              limit:int=10,
              tag:Optional[str]=Query(None, description="Filter notes by tag")):
    query = db.query(models.Note)
    if tag:
        query = query.filter(models.Note.tag.like(f"%{tag}%"))

    notes = query.offset(skip).limit(limit).all()
    return notes

@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note(note_id:int=Path(..., description="The ID of the note to retrieve"), db:Session=Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/", response_model=schemas.NoteResponse)
def create_note(note:schemas.NoteCreate, db:Session=Depends(get_db)):
    db_note = models.Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.put("/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int = Path(..., description="The ID of the note to update"),
    note: schemas.NoteUpdate = ...,
    db: Session = Depends(get_db)
):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in note.dict(exclude_unset=True).items():
        setattr(db_note, key, value)
    db.commit()
    db.refresh(db_note)
    return db_note


@router.delete("/{note_id}", response_model=dict)
def delete_note(note_id:int=Path(..., description="The ID of the note to delete"), db:Session=Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(db_note)
    db.commit()
    return {"detail": "Note deleted"}

