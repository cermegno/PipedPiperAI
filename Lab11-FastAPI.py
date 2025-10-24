# Introduction to FastAPI

# First import the necessary libraries
# - uvicorn is used to implement the web server
# - the fastapi library itself
# - pydantic is used to define and enforce the schema of the JSON payload of POST calls. It is used for the the SWAGGER docs 
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# This is the definition of the schema
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# Create a FastAPI server instance
app = FastAPI()

# Simple route for diagnostic purposes that tells use the server is running
@app.get("/status")
async def status():
    return {"message": "I am running"}

# POST route to create an item. We are not adding any code to create anything, we are just testing the routes
@app.post("/items/")
async def create_item(item: Item):
    #Do something here to create an item
    return item

# We don't need to define a route for the Swagger documentation. It is created automatically under "/docs"

# Finally we run the server. We can specify the IP and port to listen to.
# We can use the workers parameter to multithread it. For containers the best practice is a single worker and scale the amount of containers
uvicorn.run(app,host='0.0.0.0', port=8000, workers=1)

# You can try the following in a browser
# http://172.24.167.20:8000/         # Not found because we haven't specified a "/" route
# http://172.24.167.20:8000/status   # "I am running" message
# http://172.24.167.20:8000/items/   # "Method not allowed". The URL matches a route but the browser is sending a GET call instead of a POST
# http://172.24.167.20:8000/docs     # It will show the Swagger documentation
