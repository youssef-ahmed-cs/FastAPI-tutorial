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
