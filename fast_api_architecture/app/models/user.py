from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

# User model with an optional unique ID
class User(BaseModel):
    id: Optional[UUID] = None
    username: str
    email: str
