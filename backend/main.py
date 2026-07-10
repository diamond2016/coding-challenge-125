from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from src.diff.myers_diff import MyersDiff

app = FastAPI(title="Diff API", version="1.0.0")

# Request model
class DiffPrettypRequest(BaseModel):
    string_a: str
    string_b: str

# Response model
class DiffPrettypResponse(BaseModel):
    diff: Optional[str]

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# Initialize diff object
diff_obj = MyersDiff()

@app.post("/api/diff-prettyp/", response_model=DiffPrettypResponse)
async def diff_prettyp(request: DiffPrettypRequest):
    """
    Compute prettyp diff between two strings.
    
    Returns ANSI color-coded diff where:
    - Red (0): deleted characters
    - Green (1): inserted characters  
    - Cyan (6): equal characters
    """
    result = diff_obj.myers_diff_prettyp(request.string_a, request.string_b)
    return DiffPrettypResponse(diff=result)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
