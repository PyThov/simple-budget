from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *
import psycopg2
import logging

logging.basicConfig(filename='backend/db/db.log', encoding='utf-8', level=logging.DEBUG)

# Setup Database
engine = create_engine("postgresql://simpleuser:complexpassword@localhost/simpledb", echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def getEngine():
    return 

# Initializes the database tables
# Will not overwrite existing tables / data
def initializeDB():
    logging.debug("Initializing database")
    try:
        Base.metadata.create_all(engine)
        logging.debug("Successfully initialized tables.")
    except Exception as e:
        logging.error(f"Error creating tables: {e}")
