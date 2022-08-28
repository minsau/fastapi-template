from typing import List, Optional
from pydantic import EmailStr
from sqlmodel import Field, Relationship, UniqueConstraint
from app.core.base_class import Base



class User(Base, table=True):
    __table_args__ = (UniqueConstraint('email', name='user_email_unique'),)
    full_name: Optional[str] = None
    email: EmailStr = Field(index=True, nullable=False)
    hashed_password:str = Field(nullable=False)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)