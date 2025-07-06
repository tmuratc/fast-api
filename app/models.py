from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime, UTC
import uuid

Base = declarative_base()

class Clan(Base):
    __tablename__ = "clans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    region = Column(String(10), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC), nullable=False)

