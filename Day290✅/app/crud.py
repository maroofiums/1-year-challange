from sqlalchemy.orm import Session
import models,schemas

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db:Session):
    return db.query(models.Todo).all()

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not db_todo:
        return None

    if todo_update.title is not None:
        db_todo.title = todo_update.title
    if todo_update.completed is not None:
        db_todo.completed = todo_update.completed

    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    if not db_todo:
        return None

    db.delete(db_todo)
    db.commit()
    return db_todo

