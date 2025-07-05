import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Clan

# Geçici in-memory SQLite DB
engine = create_engine("sqlite:///:memory:", echo=False)
SessionLocal = sessionmaker(bind=engine)

def setup_module(module):
    # Tabloyu test başında oluştur
    Base.metadata.create_all(bind=engine)

def test_clan_model_insert_and_fetch():
    db = SessionLocal()

    new_clan = Clan(name="Test Klan", region="TR")
    db.add(new_clan)
    db.commit()

    result = db.query(Clan).first()

    assert result.id is not None
    assert isinstance(result.id, uuid.UUID)
    assert result.name == "Test Klan"
    assert result.region == "TR"
    assert result.created_at is not None
