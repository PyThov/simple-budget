from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base

class Savings(Base):
    __tablename__ = "savings"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    emg_savings = Column(Float)
    
    users = relationship("Users", back_populates="savings")

    def __repr__(self) -> str:
        return f"Savings(id={self.id!r})"
