# Online Diff Viewer

A web application for comparing two text inputs using the Myers Diff algorithm.
See "Coding Callenge #125" by J. Crickett [link](https://codingchallenges.substack.com/p/coding-challenge-125-online-diff)

## Quick Start

### Prerequisites

Install **pnpm** and **uv**:

```bash
# pnpm (for frontend)
npm install -g pnpm

# uv (for backend)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

```bash
# Install all dependencies
pnpm install
```

### Development

```bash
# Run both frontend and backend
pnpm dev

# Or run separately
pnpm frontend:dev    # Frontend on http://localhost:5173
pnpm backend:dev     # Backend on http://localhost:8000
```

### Testing

```bash
# Run all tests
pnpm test

# Or run separately
pnpm test:frontend   # Frontend tests
pnpm test:backend    # Backend tests
```

## Architecture

See [ARCHITECTURE.md](apps/shared/docs/ARCHITECTURE.md) for detailed documentation.

## Tech Stack

- **Frontend**: Vue 3 + Vite + TypeScript
- **Backend**: FastAPI + Python 3.11+
- **Diff Algorithm**: Myers Diff (character-level)

## API

### Compute Diff

```bash
curl -X POST http://localhost:8000/api/diff \
  -H "Content-Type: application/json" \
  -d '{"string_a": "ABCD", "string_b": "ABECD"}'
```

Response:
```json
{
  "diff": "<span style='background-color:#f2f6f4'>A</span><span style='background-color:#f2f6f4'>B</span><span style='background-color:#d5f5e3'>E</span><span style='background-color:#f2f6f4'>C</span><span style='background-color:#f2f6f4'>D</span>"
}
```

## Example
![example image diff in home page](home-step1.png)
## License

[MIT](./LICENSE)
