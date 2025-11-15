# models/coe_info.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class COEInfo(Base):
    __tablename__ = "coe_info"

    # Id of the COE Entry
    id = Column(Integer, primary_key=True, index=True)
    # Id of the Car for this COE Entry
    car_id = Column(Integer, ForeignKey("cars.id"))
    coe_category = Column(String)
    coe_quota_premium = Column(Float)
    coe_expiry_date = Column(Date)

    # Relationship to Car
    car = relationship("Car", back_populates="coe_info")
