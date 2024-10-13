from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.task_service import (
    create_task, get_tasks, get_task_by_id, update_task, delete_task
)
from db import get_db

router = APIRouter()

@router.post("/tasks/")
def create_new_task(title: str, description: str, db: Session = Depends(get_db)):
    return create_task(db, title, description)

@router.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}")
def update_existing_task(task_id: int, title: str, description: str, db: Session = Depends(get_db)):
    task = update_task(db, task_id, title, description)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
