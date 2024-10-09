from fastapi import HTTPException
from uuid import UUID, uuid4
from typing import List
from ..models.task import Task

# In-memory list to store tasks
tasks: List[Task] = []

# Function to create a new task
def create_task(task_data: Task) -> Task:
    task_data.id = uuid4()  # Generate a unique ID for the task
    tasks.append(task_data)
    return task_data

# Function to get all tasks
def get_all_tasks() -> List[Task]:
    return tasks

# Function to get a specific task by ID
def get_task(task_id: UUID) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")  # Raise exception if not found

# Function to update an existing task by ID
def update_task(task_id: UUID, task_update: Task) -> Task:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[index] = updated_task  # Replace the old task with the updated one
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")  # Raise exception if not found

# Function to delete a task by ID
def delete_task(task_id: UUID) -> bool:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)  # Remove the task from the list
            return True  # Return True if deletion was successful
    raise HTTPException(status_code=404, detail="Task not found")  # Raise exception if not found
