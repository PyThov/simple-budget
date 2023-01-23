from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from constants import API_PREFIX, USER_ID
from database import SessionLocal
import api_models
import crud

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get(f"{API_PREFIX}/budget")
def get_budget(category: str, month: int, year: int, db: Session = Depends(get_db)) -> api_models.Budget:
    match category:
        case "income":
            db_result = crud.get_income(db, USER_ID, year)
        case "expenses":
            db_result = crud.get_expenses(db, USER_ID, year, month)
        case "savings":
            db_result = crud.get_savings(db, USER_ID, year, month)
        case "recreational":
            db_result = crud.get_recreational(db, USER_ID, year, month)
        case _:
            db_result = None

    if db_result is None:
        raise HTTPException(status_code=404, detail=f"Budget for {category} not found")
    return db_result

@app.post(f"{API_PREFIX}/source")
def create_source():
    return {"message": "Hello from Simple Budget!"}

@app.put(f"{API_PREFIX}/source")
def update_source():
    return {"message": "Hello from Simple Budget!"}

@app.delete(f"{API_PREFIX}/source")
def delete_source(category: str, month: int, source: str):
    return {"message": "Hello from Simple Budget!"}

@app.get(f"{API_PREFIX}/aggregated")
def get_aggregated_data(year: int) -> api_models.Aggregated:
    aggregatedData: api_models.Aggregated = {
        "tbd": None
    }
    return aggregatedData
