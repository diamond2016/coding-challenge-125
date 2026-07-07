from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Online Diff Viewer API",
    description="API backend for computing diffs, managing sessions, and fetching external files.",
    version="1.0.0",
)

# Configure CORS
# In development, we allow requests from the standard Vite dev port.
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
def health_check():
    """Health check endpoint to verify backend status."""
    return {"status": "healthy", "service": "online-diff-viewer-api"}


@app.get("/")
def read_root():
    """Welcome endpoint."""
    return {"message": "Welcome to the Online Diff Viewer API!"}
