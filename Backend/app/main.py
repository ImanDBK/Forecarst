from fastapi import FastAPI, Depends
from app import models
from app.api import users_router

# Initialize FastAPI app
app = FastAPI()

# Create database tables in ProstgreSQL
models.Base.metadata.create_all(bind=models.engine)

app.include_router(users_router, prefix="/users", tags=["users"])

