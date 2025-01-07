from typing import Any, Optional
from pydantic import Field
from .base_model import BaseModel


class Me(BaseModel):
    """@public"""
    me: Optional['MeMe']


class MeMe(BaseModel):
    """@public"""
    id: Any
    email: str
    name: str
    created_at: int = Field(alias='createdAt')


Me.model_rebuild()
