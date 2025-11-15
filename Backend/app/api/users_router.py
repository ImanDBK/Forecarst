from http.client import HTTPException
from fastapi import APIRouter, Depends
from app.core.database import get_db
from app.main import app
from app.schemas.user import User, UserResponse

router = APIRouter(prefix="/api/users", tags=["users"])
@app.post("/register", response_model=UserResponse)
async def create_user(user: User, db=Depends(get_db)):
    # Check if user with the same email already exists
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    new_user = create_user(db, user)
    return new_user