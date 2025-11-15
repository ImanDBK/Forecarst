# models/listing.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    source_site = Column(String)
    listing_url = Column(String)
    listed_price = Column(Float)
    mileage_km = Column(Integer)
    owner_count = Column(Integer)
    listed_at = Column(DateTime(timezone=True), server_default=func.now())

    car = relationship("Car", back_populates="listings")
    seller = relationship("Seller", back_populates="listings")
    predictions = relationship("Prediction", back_populates="listing")