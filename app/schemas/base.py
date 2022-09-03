from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class BaseSchema(BaseModel):
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None


class BaseInDBSchema(BaseSchema):
    id: int
    uuid: Optional[Union[str, UUID]] = None
