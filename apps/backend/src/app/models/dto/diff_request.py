from pydantic import BaseModel, Field
from typing import Annotated

NonEmptyStr = Annotated[str, Field(min_length=1)]

# Request model
class DiffRequest(BaseModel):
    string_a: NonEmptyStr
    string_b: NonEmptyStr
