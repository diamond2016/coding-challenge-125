from pydantic import BaseModel
from typing import Optional

# Response model
class DiffResponse(BaseModel):
    diff: Optional[str]
