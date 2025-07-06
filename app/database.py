from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Base
from contextlib import contextmanager
import os
#from dotenv import load_dotenv

#load_dotenv()

# Local development (SQLite)
# DATABASE_URL = "sqlite:///clans.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Production / Cloud SQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
