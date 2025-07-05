import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base
from app.database import get_db  

# Test veritabanını oluştur
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Tabloları oluştur
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override'ı uygula
app.dependency_overrides[get_db] = override_get_db

# Test client fixture
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
