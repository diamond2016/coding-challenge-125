from pydantic import BaseModel, Field
from typing import Annotated

Str = Annotated[str, Field(min_length=0)]

# Request model
class DiffRequest(BaseModel):
    string_a: Str
    string_b: Str
