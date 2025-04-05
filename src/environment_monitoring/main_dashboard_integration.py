
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the dashboard as a static file directory
app.mount("/dashboard", StaticFiles(directory="dashboard"), name="dashboard")
