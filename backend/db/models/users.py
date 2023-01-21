from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    income = relationship("Income", back_populates="users")
    expenses = relationship("Expenses", back_populates="users")
    savings = relationship("Savings", back_populates="users")
    recreational = relationship("Recreational", back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"
