from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter(prefix="/", tags=["root"])

@router.get("/", response_class=Response)
def base():
    """Welcome endpoint."""
    return {"message": "Welcome to the Online Diff Viewer API!"}
