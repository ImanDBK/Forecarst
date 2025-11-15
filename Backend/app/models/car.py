from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class car(Base):
    __tablename__ = "cars"

    # Primary Key is the Unique identifier for each car in the database
    # Index is used to speed up queries on this column
    id = Column(Integer, primary_key=True, index=True)

    # Make, Model, Year, and Owner ID of the car
    make = Column(String, index=True, nullable=False)
    model = Column(String, index=True, nullable=False)
    year = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)