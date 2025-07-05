from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime, UTC

class ClanCreate(BaseModel):
    name: str
    region: Optional[str] = None

class ClanOut(BaseModel):
    id: UUID
    name: str
    region: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)