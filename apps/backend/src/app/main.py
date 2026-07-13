from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.diff import router as diff_router
from app.api.routes.root import router as root_router

app = FastAPI(
    title="Online Diff Viewer API",
    version="1.0.0",
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register other routes
app.include_router(root_router)
app.include_router(health_router)
app.include_router(diff_router)