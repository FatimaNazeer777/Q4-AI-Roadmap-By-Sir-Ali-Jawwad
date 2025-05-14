from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator
from datetime import date
from typing import Optional, List

app = FastAPI()

# Fake databases (just Python dictionaries for now)
users = {}
tasks = {}

user_id_counter = 1
task_id_counter = 1

# -------------------------------
# 📦 Data Models
# -------------------------------

# User creation input
class NewUser(BaseModel):
    username: str
    email: EmailStr

# User info response
class User(BaseModel):
    id: int
    username: str
    email: EmailStr

# Task input
class NewTask(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int

    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date can't be in the past.")
        return v

# Task response
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: int

# Task status update
class TaskStatus(BaseModel):
    status: str

    @validator("status")
    def valid_status(cls, v):
        if v not in ["pending", "in_progress", "completed"]:
            raise ValueError("Status must be: pending, in_progress, or completed")
        return v

# -------------------------------
# 👤 User Routes
# -------------------------------

@app.post("/users/", response_model=User)
def create_user(user: NewUser):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    users[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# -------------------------------
# 📋 Task Routes
# -------------------------------

@app.post("/tasks/", response_model=Task)
def create_task(task: NewTask):
    global task_id_counter
    if task.user_id not in users:
        raise HTTPException(status_code=404, detail="User ID not found")
    task_data = task.dict()
    task_data["id"] = task_id_counter
    task_data["status"] = "pending"
    tasks[task_id_counter] = task_data
    task_id_counter += 1
    return task_data

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: TaskStatus):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id]["status"] = status.status
    return tasks[task_id]

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in tasks.values() if task["user_id"] == user_id]
