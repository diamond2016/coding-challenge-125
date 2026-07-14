# Online Diff Viewer - Architecture

## Overview

This is a monorepo for an online diff viewer application, comparing two text inputs using the Myers Diff algorithm.

### Tech Stack

- **Frontend**: Vue 3 + Vite + TypeScript
- **Backend**: FastAPI + Python 3.11+
- **Package Managers**: 
  - Frontend: pnpm (npm ecosystem)
  - Backend: uv (modern Python package manager)
- **Diff Algorithm**: Myers Diff (forward-only, character-level)

## Directory Structure

```
coding-challenge-125/
├── apps/
│   ├── backend/              # Python + uv
│   │   ├── pyproject.toml    # Python dependencies & metadata
│   │   ├── src/
│   │   │   └── app/
│   │   │       ├── api/      # API routes
│   │   │       ├── models/   # Pydantic models
│   │   │       └── utils/    # Utility functions
│   │   │       └── main.py   # FastAPI application
│   │   └── tests/            # Backend tests
│   └── frontend/             # JavaScript + pnpm
│       ├── package.json      # npm-style dependencies
│       ├── src/
│       │   ├── api/          # API client (generated)
│       │   ├── components/   # Vue components
│       │   ├── views/        # Page views
│       │   └── App.vue       # Root component
│       └── index.html
├── apps/shared/
│   ├── openapi/
│   │   └── v1/
│   │       └── openapi.yaml  # OpenAPI specification
│   └── docs/
│       ├── ARCHITECTURE.md   # This file
│       └── api.md            # API documentation
├── pnpm-workspace.yaml       # pnpm workspace config
├── package.json              # Root scripts (pnpm only)
└── README.md                 # Quick start guide
```

## Package Manager Strategy

### Frontend: pnpm

The frontend uses **pnpm** for dependency management, following the npm ecosystem conventions.

**Why pnpm?**
- Fast installation (hard links)
- Disk space efficient
- Compatible with npm packages
- Excellent monorepo support

**Commands:**
```bash
pnpm install              # Install dependencies
pnpm dev                  # Start development server
pnpm build                # Build for production
pnpm test                 # Run tests
```

### Backend: uv

The backend uses **uv** for Python dependency management, a modern, fast alternative to pip/poetry.

**Why uv?**
- Blazing fast (written in Rust)
- Single binary (no installation needed)
- Built-in virtual environment management
- Seamless pip/conda compatibility
- Modern Python packaging (PEP 621/pyproject.toml)

**Commands:**
```bash
uv sync                   # Install dependencies (creates .venv)
uv run <command>          # Run command in virtual environment
uv add <package>          # Add dependency
uv remove <package>       # Remove dependency
uv export                 # Export to requirements.txt
```

### Root: package.json

The root `package.json` uses **pnpm** for coordinating both frontend and backend development.

**Why?**
- Unified entry point for development
- pnpm workspaces for frontend
- Shell commands for backend (uv)
- Concurrent execution of both services

## Development Workflow

### Prerequisites

1. **Node.js** (v18+) and **pnpm**
   ```bash
   npm install -g pnpm
   ```

2. **uv** (Python package manager)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Or using pip
   pip install uv
   ```

3. **Python** (3.11+)

### Installation

```bash
# Install frontend dependencies (pnpm)
pnpm install

# Install backend dependencies (uv)
cd apps/backend && uv sync
```

### Running Development Servers

```bash
# Run both frontend and backend concurrently
pnpm dev

# Run frontend only
pnpm frontend:dev

# Run backend only
pnpm backend:dev
```

**Ports:**
- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`

### Running Tests

```bash
# Run all tests
pnpm test

# Run frontend tests only
pnpm test:frontend

# Run backend tests only
pnpm test:backend
```

### Building for Production

```bash
# Build frontend
pnpm build

# Backend is already production-ready (FastAPI)
```

## uv Quick Start

### Installation

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

### Basic Commands

```bash
# Initialize a new project
uv init my-project

# Install dependencies
uv add fastapi uvicorn

# Add dev dependencies
uv add --dev pytest black

# Run a command in the virtual environment
uv run python script.py

# Sync dependencies (creates .venv)
uv sync

# Export to requirements.txt
uv export -o requirements.txt
```

### Virtual Environment Management

uv automatically manages virtual environments:

```bash
# uv sync creates .venv in project root
cd my-project
uv sync

# uv run activates .venv automatically
uv run python script.py

# View virtual environment path
uv venv show
```

### Migration from pip/poetry

```bash
# Convert pyproject.toml to uv format
uv lock

# Install all dependencies
uv sync

# Export requirements.txt
uv export -o requirements.txt

# Use uv instead of pip
# OLD: pip install fastapi
# NEW: uv add fastapi

# OLD: pip freeze > requirements.txt
# NEW: uv export -o requirements.txt
```

## pnpm Quick Start

### Installation

```bash
npm install -g pnpm
```

### Workspace Commands

```bash
# Install all dependencies
pnpm install

# Run command in specific package
pnpm --filter frontend run dev
pnpm --filter coding-challenge-125-backend run dev

# Run command in all packages
pnpm run dev
```

### Filter Syntax

- `pnpm --filter <name>` - Run in specific package
- `pnpm --filter <name>...` - Run in multiple packages
- `pnpm --filter @scope/*` - Run in all packages with scope

## Troubleshooting

### Port Already in Use

**Backend port 8000:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
# Or on macOS
lsof -ti:8000 | xargs sudo kill -9
```

**Frontend port 5173:**
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9
```

### uv Not Found

```bash
# Check installation
which uv

# Add to PATH (if needed)
# macOS/Linux: ~/.local/bin is usually added automatically
# Windows: Add C:\Users\<user>\.local\bin to PATH
```

### pnpm Not Found

```bash
# Reinstall pnpm
npm install -g pnpm

# Verify installation
pnpm --version
```

### Dependency Conflicts

**Backend:**
```bash
# Clear uv cache and sync
uv self update
uv cache clean
uv sync
```

**Frontend:**
```bash
# Clear pnpm cache and reinstall
pnpm store prune
pnpm install
```

### CORS Issues

Ensure backend CORS allows frontend origin:
```python
# apps/backend/src/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## API Endpoints

### Backend API

- `GET /` - Root endpoint
- `GET /health/` - Health check
- `POST /api/diff` - Compute diff between two strings

### Frontend API Client

Generated from OpenAPI specification at `apps/shared/openapi/v1/openapi.yaml`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pnpm test`
5. Submit a pull request

## License

MIT
