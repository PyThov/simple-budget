from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base

class Expenses(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    
    users = relationship("Users", back_populates="expenses")

    def __repr__(self) -> str:
        return f"Expenses(id={self.id!r})"
