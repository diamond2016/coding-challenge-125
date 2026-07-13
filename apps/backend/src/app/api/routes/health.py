from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint to verify backend status."""
    return {"status": "healthy", "service": "online-diff-viewer-api"}