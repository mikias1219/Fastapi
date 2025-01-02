from fastapi import FastAPI
import start

app = FastAPI()

# Include routes from the 'start' module
app.include_router(start.router)

# Define the root route
@app.get("/")
async def root():
    return {"message": "Hello World"}
