from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="Root endpoint that returns a greeting message.")
async def read_root():
    return {"Hello": "World"}


@app.post('/', description="Endpoint to create a new item.")
async def post():
    return {"item_created"}


@app.put('/', description="Endpoint to update an existing item.")
async def put():
    return {"item_updated"}
