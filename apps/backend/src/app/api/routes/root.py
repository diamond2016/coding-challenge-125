from fastapi import APIRouter

router = APIRouter(tags=["root"])

@router.get("/")
def get_home():
    """Root endpoint."""
    return {"message": "Welcome to the Online Diff Viewer API!"}