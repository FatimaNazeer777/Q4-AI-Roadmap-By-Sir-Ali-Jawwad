# Task Tracker API

A FastAPI-based REST API for managing users and their tasks. This API provides endpoints for creating and managing users, as well as creating, updating, and retrieving tasks.

## Features

- User Management
  - Create new users
  - Retrieve user information
- Task Management
  - Create new tasks
  - Update task status
  - Retrieve task details
  - Get all tasks for a specific user
- Data Validation
  - Email validation
  - Due date validation (cannot be in the past)
  - Task status validation

## API Endpoints

### Users

- `POST /users/` - Create a new user
  - Required fields: username, email
- `GET /users/{user_id}` - Get user information by ID

### Tasks

- `POST /tasks/` - Create a new task
  - Required fields: title, due_date, user_id
  - Optional fields: description
- `GET /tasks/{task_id}` - Get task information by ID
- `PUT /tasks/{task_id}` - Update task status
  - Valid status values: "pending", "in_progress", "completed"
- `GET /users/{user_id}/tasks` - Get all tasks for a specific user

## Data Models

### User
```python
{
    "id": int,
    "username": str,
    "email": EmailStr
}
```

### Task
```python
{
    "id": int,
    "title": str,
    "description": Optional[str],
    "due_date": date,
    "status": str,
    "user_id": int
}
```

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## Dependencies

- FastAPI
- Pydantic
- Email-validator
- Uvicorn

## Note

This is a development version using in-memory storage (Python dictionaries). For production use, consider implementing a proper database backend.
