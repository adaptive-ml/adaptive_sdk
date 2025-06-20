from io import IOBase
from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict

class UnsetType:
    """@private"""

    def __bool__(self) -> bool:
        return False
UNSET = UnsetType()

class BaseModel(PydanticBaseModel):
    """@private"""
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True, arbitrary_types_allowed=True, protected_namespaces=())

class Upload:
    """@private"""

    def __init__(self, filename: str, content: IOBase, content_type: str):
        self.filename = filename
        self.content = content
        self.content_type = content_type