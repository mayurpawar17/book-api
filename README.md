# Book API

Simple FastAPI-based Book API.

## Prerequisites

- Python 3.9 (the project is tested with Python 3.9)
- git (optional)

## Setup

1. From the project root, create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies. If a requirements file exists, run:

   pip install -r requirements.txt

   If there is no requirements file, install at least the basics:

   pip install fastapi uvicorn

## Run the application

From the project root (recommended):

   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

Notes:
- Use the module path `app.main:app` when running from the repository root so the application imports correctly.
- If you `cd` into the `app/` directory, use `uvicorn main:app --reload` instead.
- If you get an `Address already in use` error, another server is running on the same port. Find and stop it (e.g., `lsof -nP -iTCP -sTCP:LISTEN | grep 8000` and then `kill <PID>`).

## Import / package notes

- This project relies on standard Python import behavior. Python 3.3+ supports implicit namespace packages (no `__init__.py`) so imports like `from app.modules.books import ...` should work when starting the process from the project root.
- If tools or launch contexts fail to resolve `app` (e.g., `ModuleNotFoundError: No module named 'app'`), either:
  - Ensure you run commands from the project root (so the root is on `sys.path`), or
  - Add an empty `__init__.py` file to the package directories (`app/`, `app/modules/`, etc.) to force explicit package semantics.

## Python compatibility

- The codebase is written to be compatible with Python 3.9. Avoid using Python 3.10-only syntax (for example, `X | None` union types) unless you run the app with Python 3.10+.

## Stopping the server

- When running with `--reload`, uvicorn will spawn watcher processes. To stop a running server, either use Ctrl+C in the terminal that started it, or find the process and kill it:

  lsof -nP -iTCP -sTCP:LISTEN | grep 8000
  kill <PID>

## Troubleshooting

- `ModuleNotFoundError: No module named 'app'`:
  - Make sure you're running from the project root and using the `app.main:app` import path.
  - If the problem persists in certain tools (editors, CI), add `__init__.py` files to the package folders as described above.

- `RuntimeError: The starlette.testclient module requires the httpx package to be installed.`
  - Install test dependencies: `pip install httpx` (and any test requirements used by the project).

## Development notes

- The API root is mounted at `/api/v1/books` and a health endpoint is available at `/health`.

