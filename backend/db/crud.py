from sqlalchemy.orm import Session
from backend.api import models as api_models
from backend.db import models as db_models

def get_income(db: Session, user_id: int, year: int):
    return db.query(db_models.Income).filter(db_models.Income.user_id == user_id, db_models.Income.year == year).first()
