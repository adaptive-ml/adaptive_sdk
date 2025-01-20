from typing import Any, Optional
from pydantic import Field
from .base_model import BaseModel


class DescribeMe(BaseModel):
    """@public"""
    me: Optional['DescribeMeMe']


class DescribeMeMe(BaseModel):
    """@public"""
    id: Any
    email: str
    name: str
    created_at: int = Field(alias='createdAt')


DescribeMe.model_rebuild()
