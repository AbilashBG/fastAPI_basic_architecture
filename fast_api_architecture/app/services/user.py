from fastapi import HTTPException
from uuid import UUID, uuid4
from typing import List
from ..models.user import User

# In-memory list to store users
users: List[User] = []

# Function to create a new user
def create_user(user_data: User) -> User:
    user_data.id = uuid4()  # Generate a unique ID for the user
    users.append(user_data)
    return user_data

# Function to get all users
def get_all_users() -> List[User]:
    return users

# Function to get a specific user by ID
def get_user(user_id: UUID) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")  # Raise exception if not found

# Function to update an existing user by ID
def update_user(user_id: UUID, user_update: User) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            updated_user = user.copy(update=user_update.dict(exclude_unset=True))
            users[index] = updated_user  # Replace the old user with the updated one
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")  # Raise exception if not found

# Function to delete a user by ID
def delete_user(user_id: UUID) -> bool:
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)  # Remove the user from the list
            return True  # Return True if deletion was successful
    raise HTTPException(status_code=404, detail="User not found")  # Raise exception if not found
