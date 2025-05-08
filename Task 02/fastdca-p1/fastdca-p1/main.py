from fastapi import FastAPI

app = FastAPI()

# This runs when you go to the home page "/"
@app.get("/")
def read_root():
    return {"Hello from Fatima!"}

# This runs when you go to "/items/{some_id}"
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
