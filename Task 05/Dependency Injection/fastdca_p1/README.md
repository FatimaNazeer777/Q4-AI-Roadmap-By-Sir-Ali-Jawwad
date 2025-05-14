# FastAPI Dependency Injection Examples

This project demonstrates various ways to implement dependency injection in FastAPI applications. It showcases different patterns and use cases for dependencies in FastAPI.

## Features

- Simple dependency injection
- Dependencies with parameters
- Dependencies with query parameters
- Multiple dependencies
- Class-based dependencies
- Error handling with dependencies

## API Endpoints

### 1. Simple Dependency
- **Endpoint**: `/get-simple-goal`
- **Method**: GET
- **Description**: Returns a simple goal message using a basic dependency

### 2. Dependency with Parameters
- **Endpoint**: `/get-goal`
- **Method**: GET
- **Description**: Returns a goal message with username using parameterized dependency

### 3. Dependency with Query Parameters
- **Endpoint**: `/signin`
- **Method**: GET
- **Query Parameters**:
  - `username`: String
  - `password`: String
- **Description**: Simple login simulation using query parameters

### 4. Multiple Dependencies
- **Endpoint**: `/main/{num}`
- **Method**: GET
- **Path Parameter**: `num` (integer)
- **Description**: Demonstrates how to use multiple dependencies in a single endpoint

### 5. Class-based Dependencies
- **Endpoint**: `/blog/{id}`
- **Method**: GET
- **Path Parameter**: `id` (string)
- **Description**: Returns blog content using a class-based dependency

- **Endpoint**: `/user/{id}`
- **Method**: GET
- **Path Parameter**: `id` (string)
- **Description**: Returns user information using a class-based dependency

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

## Running the Application

To run the application, use the following command:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## Error Handling

The application includes error handling for:
- 404 Not Found errors for invalid blog or user IDs
- Invalid query parameters
- Authentication failures

## Dependencies

- FastAPI
- Uvicorn (ASGI server)
- Python 3.x

## License

This project is open source and available under the MIT License.
