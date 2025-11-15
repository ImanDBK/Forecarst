from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    # Primary Key is the Unique identifier for each user in the database
    # Index is used to speed up queries on this column
    id = Column(Integer, primary_key=True, index=True)

    # Username, Email, Password and Active status of the user
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)