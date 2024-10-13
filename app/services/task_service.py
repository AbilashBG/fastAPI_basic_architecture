from sqlalchemy.orm import Session
from ..models.task import Task

# Create a new task
def create_task(db: Session, title: str, description: str):
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get all tasks
def get_tasks(db: Session):
    return db.query(Task).all()

# Get a task by ID
def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# Update a task
def update_task(db: Session, task_id: int, title: str, description: str):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        db.commit()
        db.refresh(task)
    return task

# Delete a task
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
