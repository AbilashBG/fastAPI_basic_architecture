from fastapi import FastAPI
from app.routes import task_route
from db import Base, engine

# Initialize the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the task routes
app.include_router(task_route.router)
