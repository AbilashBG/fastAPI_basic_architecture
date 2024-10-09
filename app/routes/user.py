from fastapi import APIRouter, HTTPException
from uuid import UUID
from typing import List
from ..models.user import User
from app.services import user as user_service

router = APIRouter()

# Route to get all users
@router.get("/", response_model=List[User])
def fetch_all_users():
    return user_service.get_all_users()

# Route to create a new user
@router.post("/", response_model=User)
def create_new_user(user: User):
    return user_service.create_user(user)

# Route to get a specific user by ID
@router.get("/{user_id}", response_model=User)
def fetch_user(user_id: UUID):
    return user_service.get_user(user_id)

# Route to update a specific user by ID
@router.put("/{user_id}", response_model=User)
def modify_user(user_id: UUID, user_update: User):
    return user_service.update_user(user_id, user_update)

# Route to delete a specific user by ID
@router.delete("/{user_id}")
def remove_user(user_id: UUID):
    user_service.delete_user(user_id)
    return {"detail": "User deleted successfully"}
