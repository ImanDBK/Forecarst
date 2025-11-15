from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlachemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from backend.app.core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    # Try to open and (finally) close the database session
    try:
        yield db
    finally:
        db.close()

# Define a type annotation for database session dependency
db_dependency = Annotated[Session, Depends(get_db)]
