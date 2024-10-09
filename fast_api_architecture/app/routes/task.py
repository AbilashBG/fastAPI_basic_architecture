from fastapi import APIRouter
from uuid import UUID
from typing import List
from ..models.task import Task
from app.services import task as task_service 

router = APIRouter()

# Route to get all tasks
@router.get("/", response_model=List[Task])
def fetch_all_tasks():
    return task_service.get_all_tasks()

# Route to create a new task
@router.post("/", response_model=Task)
def create_new_task(task: Task):
    return task_service.create_task(task)

# Route to get a specific task by ID
@router.get("/{task_id}", response_model=Task)
def fetch_task(task_id: UUID):
    return task_service.get_task(task_id)

# Route to update a specific task by ID
@router.put("/{task_id}", response_model=Task)
def modify_task(task_id: UUID, task_update: Task):
    return task_service.update_task(task_id, task_update)

# Route to delete a specific task by ID
@router.delete("/{task_id}")
def remove_task(task_id: UUID):
    task_service.delete_task(task_id)
    return {"detail": "Task deleted successfully"}
