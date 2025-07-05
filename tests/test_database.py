import os
from sqlalchemy import create_engine, inspect
from app.models import Base

def test_init_db_creates_clan_table():
    db_path = "test_clans.db"
    db_url = f"sqlite:///{db_path}"

    if os.path.exists(db_path):
        os.remove(db_path)

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "clans" in tables

    engine.dispose()  # bağlantıyı kapat
    os.remove(db_path)
