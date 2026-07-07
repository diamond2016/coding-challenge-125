## Step 1

**backend**
We'll use a python layer for the backend, hoping to exploit libraries and packages avalible. 

We want to adopt openapi spec driven approach, because of the language chosen we'll use fastapi, using as much as possible automated code creation

**frontend**
The frontend will use the Vue.js + typescript technology.

**template project**
We start analyzing the architecture and creating a project template. 

We want to use a monorepo approach, what are the better tools, for example for all phases of structure, devel, testing I would like for package management pnpm, ok in this context? 

Is it a correct mix Vue/js/node.js and python?.

--- DISCUSSION ON ARCHITECTURE ---

### 1. Technology Stack Analysis

#### Is Vue.js, Node.js (Vite/TypeScript), and Python (FastAPI) a correct mix?
**Yes, absolutely.** This is a highly robust and popular architecture:
*   **FastAPI (Python):** Perfect for implementing server-side diffing utilities (e.g., integrating Python's built-in `difflib`, writing custom AST-based parsers, or handling AI-driven explanations with LLMs). It automatically documents APIs with OpenAPI (Swagger) out of the box.
*   **Vue 3 (Composition API) + TypeScript:** Provides a fast, reactive UI. The diff viewer requires complex reactivity (virtualized lists, synchronized scrolling, settings triggers), and Vue handles this beautifully.
*   **The Backend Role:** Although the challenge states the viewer "runs entirely in the browser," having a backend is valuable for:
    *   **Bypassing CORS:** Fetching files from arbitrary URLs (Step 6) directly in-browser will fail due to CORS. The Python backend can act as a proxy.
    *   **Secure API Keys:** Step 16's "Going Further" suggests AI-powered diff explanations. The backend can call LLM APIs securely without exposing API keys to the browser.
    *   **Shared/Saved Sessions:** Saving named diffs (Step 14) can be synced to a backend database.

---

### 2. Monorepo Organization & Tooling

To manage both the Python and TypeScript environments, we can organize them into a clean monorepo. 

#### Recommended Directory Structure
```text
coding-challenge-125/
├── backend/                  # FastAPI Backend
│   ├── app/
│   │   ├── main.py           # Entry point
│   │   ├── api/              # API router endpoints
│   │   └── services/         # Diff logic (e.g., Myers diff, parsing)
│   ├── requirements.txt      # Python dependencies
│   └── venv/                 # Local Python virtual environment
├── frontend/                 # Vue 3 + TypeScript + Vite Frontend
│   ├── src/
│   │   ├── components/       # Diff viewers, settings panel, etc.
│   │   ├── worker/           # Web Worker for client-side diffs
│   │   └── client/           # Auto-generated OpenAPI client
│   ├── package.json
│   └── vite.config.ts
├── package.json              # Root package.json to coordinate commands
├── pnpm-workspace.yaml       # Defines workspaces for pnpm
└── README.md
```

#### How to manage this with `pnpm`?
We can use a **hybrid monorepo** approach:
1.  **Frontend/Node packages:** Managed directly by `pnpm` workspaces.
2.  **Python Backend:** Isolated in its own folder with a virtual environment (`venv`).
3.  **Root Orchestration:** The root `package.json` will use `concurrently` (or a similar tool) to run dev servers for both the frontend and backend with a single command (`pnpm dev`).

**Root `package.json` Example:**
```json
{
  "name": "online-diff-viewer-monorepo",
  "private": true,
  "scripts": {
    "dev": "concurrently \"pnpm --filter frontend dev\" \"pnpm backend:dev\"",
    "backend:dev": "cd backend && . venv/bin/activate && uvicorn app.main:app --reload",
    "openapi:generate": "curl http://localhost:8000/openapi.json > frontend/openapi.json && pnpm --filter frontend generate-client"
  },
  "devDependencies": {
    "concurrently": "^8.2.2"
  }
}
```

---

### 3. OpenAPI-Spec Driven Development

FastAPI automatically hosts an OpenAPI specification at `/openapi.json` when the server is running. We can exploit this to auto-generate fully typed TypeScript API clients on the frontend.

1.  **Define API in FastAPI:** Write Python routes using Pydantic models for request and response structures.
2.  **Generate Spec:** Start the backend.
3.  **Generate Frontend Client:** Use a tool like `@hey-api/openapi-ts` or `openapi-typescript` in the `frontend` folder to consume the `/openapi.json` and output typed fetch methods.

This means you never write manual fetch functions or define API interface types in Vue; TypeScript will automatically know the exact structure of your backend endpoints!

---

### Running app

`pnpm dev` run all concurrently

- backend localhost:8000

- frontend localhost:5173


07.07.2026: We have completed step 1- now study diff algorithm (we want to use existing libraries from python!)