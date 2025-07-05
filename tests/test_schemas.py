from app.schemas import ClanCreate, ClanOut
from uuid import uuid4
from datetime import datetime

def test_clan_create_schema():
    data = {"name": "Test Klan", "region": "US"}
    clan = ClanCreate(**data)

    assert clan.name == "Test Klan"
    assert clan.region == "US"

def test_clan_create_schema_optional_region():
    data = {"name": "NoRegionKlan"}
    clan = ClanCreate(**data)

    assert clan.name == "NoRegionKlan"
    assert clan.region is None

def test_clan_out_schema_parsing():
    test_id = uuid4()
    now = datetime.utcnow()
    data = {
        "id": test_id,
        "name": "OutKlan",
        "region": "TR",
        "created_at": now
    }

    clan = ClanOut(**data)

    assert clan.id == test_id
    assert clan.created_at == now
