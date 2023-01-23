from sqlalchemy.orm import Session
import api_models
import db_models

def add_to_db(db: Session, db_model: any) -> any:
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

# Users
def get_user(db: Session, user: api_models.User):
    return db.query(db_models.Users).filter(
        db_models.Users.id == user.id,
        db_models.Users.name == user.name
    )

# Income
def get_income(db: Session, user_id: int, year: int):
    return db.query(db_models.Income).filter(
        db_models.Income.user_id == user_id,
        db_models.Income.year == year
    ).first()

def add_income(db: Session, user_id: int, source: api_models.Source, taxrate: float):
    db_income = db_models.Income(
        user_id=user_id,
        **source.dict(),
        taxrate=taxrate
    )
    return add_to_db(db, db_income)

# Expenses
def get_expenses(db: Session, user_id: int, year: int, month: int):
    return db.query(db_models.Expenses).filter(
        db_models.Expenses.user_id == user_id,
        db_models.Expenses.year == year,
        db_models.Expenses.month == month
    ).first()

def add_expenses(db: Session, user_id: int, source: api_models.Source):
    db_expenses = db_models.Expenses(
        user_id=user_id,
        **source.dict()
    )
    return add_to_db(db, db_expenses)

# Savings
def get_savings(db: Session, user_id: int, year: int, month: int):
    return db.query(db_models.Savings).filter(
        db_models.Savings.user_id == user_id,
        db_models.Savings.year == year,
        db_models.Savings.month == month
    ).first()

def add_savings(db: Session, user_id: int, source: api_models.Source, emg_savings: float):
    db_savings = db_models.Savings(
        user_id=user_id,
        **source.dict(),
        emg_savings=emg_savings
    )
    return add_to_db(db, db_savings)

# Recreational
def get_recreational(db: Session, user_id: int, year: int, month: int):
    return db.query(db_models.Recreational).filter(
        db_models.Recreational.user_id == user_id,
        db_models.Recreational.year == year,
        db_models.Recreational.month == month
    ).first()

def add_recreational(db: Session, user_id: int, source: api_models.Source):
    db_recreational = db_models.Recreational(
        user_id=user_id,
        **source.dict()
    )
    return add_to_db(db, db_recreational)
