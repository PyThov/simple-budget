from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_models
import psycopg2

# Setup Database
engine = create_engine("postgresql://simpleuser:complexpassword@localhost/simpledb", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initializes the database tables
# Will not overwrite existing tables / data
def initializeDB():
    print("Initializing database")
    try:
        db_models.Base.metadata.create_all(bind=engine)
        print("Successfully initialized tables.")
    except Exception as e:
        print(f"Error creating tables: {e}")
