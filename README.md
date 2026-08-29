# Book API

A simple FastAPI project for serving a book API.

## Prerequisites

- Python 3.14+
- uv installed on your machine

## Install dependencies

From the project root:

```bash
uv sync
```

This installs the project and its dependencies from the `pyproject.toml` file.

## Run the project

The FastAPI app lives in the `src` directory, so run it from there:

```bash
cd src
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Useful commands

```bash
uv run python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

This is the same as the command above and can be used if you prefer running uvicorn via Python.
