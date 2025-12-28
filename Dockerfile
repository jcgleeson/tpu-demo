# Start from a small official astral Python image containing uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install curl with minimal dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup a non-root user
RUN groupadd --system --gid 999 nonroot \
 && useradd --system --gid 999 --uid 999 --create-home nonroot

# Set the working directory in the container
WORKDIR /app

# TODO: bake in the unit, linting, and formatting checks as prerequisites
# to the build process.

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# Omit development dependencies
ENV UV_NO_DEV=1
# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin

# Install the project's dependencies using the lockfile and settings
COPY --chown="nonroot:nonroot" uv.lock pyproject.toml /app/
RUN uv sync --locked --no-install-project

COPY --chown="nonroot:nonroot" ./src /app/src
RUN uv sync --locked

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
# RUN --mount=type=cache,target=/root/.cache/uv \
#     uv sync --locked

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Switch to the non-root user now that the container is configured
USER nonroot:nonroot

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Command to run the application
CMD ["fastapi", "dev", "./src/main.py"]
