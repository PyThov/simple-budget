from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

class Income(Base):
    __tablename__ = "income"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer, primary_key=True)
    taxrate = Column(Float)

    users = relationship("Users", back_populates="income")

    def __repr__(self) -> str:
        return f"Income(id={self.id!r}, user_id={self.user_id!r}, source={self.source!r}, value={self.value!r}, year={self.year!r}, taxrate={self.taxrate!r})"

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
        return f"Expenses(id={self.id!r}, user_id={self.user_id!r}, source={self.source!r}, value={self.value!r}, year={self.year!r}, month={self.month!r})"

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
        return f"Savings(id={self.id!r}, user_id={self.user_id!r}, source={self.source!r}, value={self.value!r}, year={self.year!r}, month={self.month!r}, emg_savings={self.emg_savings!r})"

class Recreational(Base):
    __tablename__ = "recreational"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    source = Column(String)
    value = Column(Float)
    year = Column(Integer)
    month = Column(Integer)
    
    users = relationship("Users", back_populates="recreational")

    def __repr__(self) -> str:
        return f"Recreational(id={self.id!r}, user_id={self.user_id!r}, source={self.source!r}, value={self.value!r}, year={self.year!r}, month={self.month!r})"
