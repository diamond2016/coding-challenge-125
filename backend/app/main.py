from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from src.diff.myers_diff import MyersDiff

from fastapi.responses import JSONResponse
import json

app = FastAPI(title="Diff API", version="1.0.0")

# Custom JSON encoder that doesn't escape escape characters
class CustomJSONEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, str):
            # For strings, don't escape the escape character
            return super().encode(obj)
        return super().encode(obj)

# Request model
class DiffPrettypRequest(BaseModel):
    string_a: str
    string_b: str

# Response model
class DiffPrettypResponse(BaseModel):
    diff: Optional[str]

app = FastAPI(
    title="Online Diff Viewer API",
    description="API backend for computing diffs, managing sessions, and fetching external files.",
    version="1.0.0",
)

# Configure CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint to verify backend status."""
    return {"status": "healthy", "service": "online-diff-viewer-api"}


@app.get("/")
def read_root() -> dict[str, str]:
    """Welcome endpoint."""
    return {"message": "Welcome to the Online Diff Viewer API!"}

# Initialize diff object
diff_obj = MyersDiff()

@app.post("/api/diff-prettyp/")
async def diff_prettyp(request: DiffPrettypRequest):
    """
    Compute prettyp diff between two strings.
    
    Returns ANSI color-coded diff where:
    - Red (0): deleted characters
    - Green (1): inserted characters  
    - Cyan (6): equal characters
    """
    result: str | None = diff_obj.myers_diff_prettyp(request.string_a, request.string_b)
    
    # Return raw JSON to avoid escaping escape characters
    return JSONResponse(content={"diff": result})
