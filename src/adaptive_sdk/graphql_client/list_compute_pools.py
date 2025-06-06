from typing import Any, List
from pydantic import Field
from .base_model import BaseModel
from .enums import ComputePoolCapability
from .fragments import PartitionData

class ListComputePools(BaseModel):
    """@public"""
    compute_pools: List['ListComputePoolsComputePools'] = Field(alias='computePools')

class ListComputePoolsComputePools(BaseModel):
    """@public"""
    id: Any
    key: str
    name: str
    created_at: int = Field(alias='createdAt')
    capabilities: List[ComputePoolCapability]
    partitions: List['ListComputePoolsComputePoolsPartitions']

class ListComputePoolsComputePoolsPartitions(PartitionData):
    """@public"""
    pass
ListComputePools.model_rebuild()
ListComputePoolsComputePools.model_rebuild()