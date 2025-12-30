# Python Project with uv and Dev Container

This project uses uv for dependency management and a dev container for development.

## Setup

1. Open the project in VS Code.
2. Install the Dev Containers extension if not already installed.
3. Use Command Palette: "Dev Containers: Reopen in Container"

This will set up the environment with Python 3.12 and uv. The virtual environment is managed by uv and located in `.venv`.

## In Development
- Open a terminal in vs code in order to interact with the development container: "Terminal -> New Terminal"
- Run the unit tests before making any changes: `uv run pytest -v ./tests/`
- Make changes, then re-run.
- Run the REST API from inside the dev container: `uv run fastapi dev --host 0.0.0.0 ./src/main.py`

## Testing in Docker Compose

- Build and run the REST API production container and a lightweight container with curl:
```
$ docker compose up --build --remove-orphans
```