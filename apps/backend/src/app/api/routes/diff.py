from fastapi import APIRouter

from app.utils.myers_diff import MyersDiff
from app.models.dto.diff_request import DiffRequest
from app.models.dto.diff_response import DiffResponse

router = APIRouter(prefix="/api", tags=["diff"])

# Initialize diff object
diff_obj = MyersDiff()

@router.post("/diff")
async def diff(request: DiffRequest) -> DiffResponse:
    """
    Compute prettyp diff between two strings.
    
    Returns HTML color-coded diff where:
    - Red background: deleted characters
    - Green background: inserted characters  
    - Neutral background: equal characters
    """
    result: str | None = diff_obj.myers_diff_prettyp(request.string_a, request.string_b)
    
    return { "diff": result }
