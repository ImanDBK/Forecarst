# models/seller.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    seller_type = Column(String)

    listings = relationship("Listing", back_populates="seller")