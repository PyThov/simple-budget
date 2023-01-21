from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .base import Base

class Recreational(Base):
    __tablename__ = "recreational"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    
    users = relationship("Users", back_populates="recreational")

    def __repr__(self) -> str:
        return f"Recreational(id={self.id!r})"
