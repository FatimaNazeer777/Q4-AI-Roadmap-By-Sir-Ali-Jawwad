# FastDCA-P1

A FastAPI-based web application that provides a simple REST API with basic endpoints.

## Features

- FastAPI framework for high-performance API development
- Python 3.11+ support
- Built-in API documentation
- Simple and clean project structure

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastdca-p1
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Running the Application

To start the development server:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative API documentation (ReDoc): `http://127.0.0.1:8000/redoc`

### Available Endpoints

1. **GET /**
   - Returns a greeting message
   - Response: `{"Hello from Fatima!"}`

2. **GET /items/{item_id}**
   - Parameters:
     - `item_id` (path parameter): Integer ID of the item
     - `q` (query parameter, optional): String query parameter
   - Response: `{"item_id": <item_id>, "q": <query_value>}`

## Development

For development, the project includes:
- pytest for testing
- pytest-asyncio for async test support

To run tests:
```bash
pytest
```