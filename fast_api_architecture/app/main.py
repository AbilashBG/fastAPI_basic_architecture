from fastapi import FastAPI
from .routes import task,user

app = FastAPI()

# Include task and user routes
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(user.router, prefix="/users", tags=["Users"])

# Root route to welcome users
@app.get("/")
def root():
    return {"message": "Hello, welcome to FastAPI!"}
