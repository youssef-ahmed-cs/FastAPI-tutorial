from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# Define various endpoints with different HTTP methods and configurations
@app.get("/", status_code=201, description="Root endpoint that returns a greeting message.")
async def read_root():
    return {"Hello": "World"}


# Define additional endpoints with various configurations
@app.post('/', description="Endpoint to create a new item.")
async def post():
    return {"item_created": "This is a new item"}


# Define additional endpoints with various configurations
@app.put('/', description="Endpoint to update an existing item.")
async def put():
    return {"item_updated"}


# Define additional endpoints with various configurations
@app.get('/users')
async def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}


# Define additional endpoints with various configurations
@app.get('/users/1', include_in_schema=False)
async def adminUser():
    return {"user": {"id": 1, "name": "User1 is here"}}


@app.get('/users/{user_id}', description="Endpoint to get a user by ID.")
async def get_user(user_id: int):
    return {"user": {"id": user_id, "name": f"User{user_id}"}}


class UserList(str, Enum):
    admin = 1
    user = 2
    moderator = 3


@app.get('/users/{user_type}/{user_id}', description="Endpoint to get user roles based on user type and ID.")
async def get_user_type(user_type: UserList, user_id: int):
    return {"user_type": user_type.name, "user_id": user_id}


items = [
    {"id": 1, "name": "c++", "price": 10.5, "status": "available"},
    {"id": 2, "name": "c", "price": 20.0, "status": "unavailable"},
    {"id": 3, "name": "php", "price": 15.75, "status": "available"},
    {"id": 4, "name": "python", "price": 30.0, "status": "available"},
    {"id": 5, "name": "java", "price": 25.0, "status": "unavailable"},
    {"id": 6, "name": "javascript", "price": 18.0, "status": "available"},
    {"id": 7, "name": "php", "price": 22.5, "status": "available"},
]


@app.get('/items', description="Endpoint to get a list of items with optional filtering by status.")
async def get_items(
        start: int = 0,
        end: int = 5,
        item_id: int = None,
        name: str = None,
):
    if item_id is not None:
        item = next((item for item in items if item["id"] == item_id), None)
        if item:
            return item
        return {"error": "Item not found"}

    if name is not None:
        filtered_items = [item for item in items if item["name"] == name]
        if filtered_items:
            return {"items": filtered_items}
        return {"error": "Item not found"}

    return {"items": items[start:end]}


@app.get('/items/prices', description="Endpoint to get items within a specified price range.")
async def sort_items(
        min_price: float = 0,
        max_price: float = 1000,
):
    filtered_items = [item for item in items if min_price <= item["price"] <= max_price]
    return {"items": filtered_items}
