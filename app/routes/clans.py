from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List, Optional
from fastapi import Query
from uuid import UUID
from fastapi import HTTPException


router = APIRouter(prefix="/clans", tags=["Clans"])

@router.post("/", response_model=schemas.ClanCreatedResponse)
def create_clan(clan: schemas.ClanCreate, db: Session = Depends(get_db)):
    new_clan = models.Clan(name=clan.name, region=clan.region)
    db.add(new_clan)
    db.commit()
    db.refresh(new_clan)
    return {"id": new_clan.id, "message": "Clan created successfully."}

@router.get("/", response_model=List[schemas.ClanOut])
def get_clans(
    region: Optional[str] = Query(None),
    sort_by_created: bool = Query(False),
    db: Session = Depends(get_db)
):
    query = db.query(models.Clan)
    if region:
        query = query.filter(models.Clan.region == region)
    if sort_by_created:
        query = query.order_by(models.Clan.created_at)
    return query.all()

@router.get("/{clan_id}", response_model=schemas.ClanOut)
def get_clan(clan_id: UUID, db: Session = Depends(get_db)):
    clan = db.query(models.Clan).filter(models.Clan.id == clan_id).first()
    if not clan:
        raise HTTPException(status_code=404, detail="Clan not found")
    return clan


@router.delete("/{clan_id}", status_code=204)
def delete_clan(clan_id: str, db: Session = Depends(get_db)):
    try:
        clan_uuid = UUID(clan_id)  # ← Burada çeviriyoruz
        clan = db.query(models.Clan).filter(models.Clan.id == clan_uuid).first()
        if not clan:
            raise HTTPException(status_code=404, detail="Clan not found")

        db.delete(clan)
        db.commit()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    except Exception as e:
        print("DELETE ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")