import uuid as uuid_lib
from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.declarative import declared_attr
from sqlmodel import Field, SQLModel


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow())
    modified_at: Optional[datetime] = Field(nullable=True, default=datetime.utcnow())
    uuid: UUID = Field(default_factory=uuid_lib.uuid4, index=True, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
