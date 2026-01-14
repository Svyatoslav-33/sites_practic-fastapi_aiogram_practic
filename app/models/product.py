from sqlalchemy import Column, Integer, String, Float
from app.database import Base 

class Product(Base):
  __table__ = "products"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(200), nullable=False)
  price = Column(Float)
  stock = Column(Integer, default=0)