# apps/backend/src/app/main.py
from fastapi import FastAPI
from api.routes.diff import diff
from api.routes.health import health
from api.routes.base import base

app = FastAPI(
    title="Online Diff Viewer API",
    version="1.0.0",
)

# This is the recommended way to organize routes
app.include_router(base.router)
app.include_router(health.router)
app.include_router(diff.router)