from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base

class Income(Base):
    __tablename__ = "income"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer)
    taxrate = Column(Float)

    users = relationship("Users", back_populates="income")

    def __repr__(self) -> str:
        return f"Income(id={self.id!r}, user_id={self.user_id!r}, source={self.source!r}, value={self.value!r}, year={self.year!r}, taxrate={self.taxrate!r})"
