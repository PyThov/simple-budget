from sqlalchemy import create_engine

def getEngine():
    return create_engine("postgresql://simpleuser:complexpassword@localhost/simpledb", echo=True, future=True)

def initializeDB():
    engine = getEngine()
    try:
        from backend.models import base, users, income, expenses, savings, recreational
        base.Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error creating tables: {e}")
    