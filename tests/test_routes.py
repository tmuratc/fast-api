import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Test veritabanı bağlantısı
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test setup: veritabanı oluşturuluyor
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Fixture: Test client
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# Testler
def test_create_clan(client):
    response = client.post("/clans/", json={
        "name": "Test Clan",
        "region": "TR"
    })
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["message"] == "Clan created successfully."

def test_get_clans(client):
    response = client.get("/clans/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any("name" in clan for clan in response.json())

def test_get_clan_by_id(client):
    create_response = client.post("/clans/", json={
        "name": "GetById Clan",
        "region": "EU"
    })
    clan_id = create_response.json()["id"]
    get_response = client.get(f"/clans/{clan_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "GetById Clan"

def test_delete_clan(client):
    create_response = client.post("/clans/", json={
        "name": "Delete Clan",
        "region": "NA"
    })
    clan_id = create_response.json()["id"]
    delete_response = client.delete(f"/clans/{clan_id}")
    assert delete_response.status_code == 204
    get_response = client.get(f"/clans/{clan_id}")
    assert get_response.status_code == 404
