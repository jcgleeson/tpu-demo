# Start from a small official Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install build deps if needed (none for this tiny project)
# Copy only requirements / pyproject first for better cache usage
COPY pyproject.toml ./

# Install dev dependency pytest so tests can run inside the image
RUN pip install --no-cache-dir "pytest"

# Copy the package and other files
COPY . .

# Make the CLI executable if needed
RUN chmod +x bin/hello || true

# Default command: run the CLI
CMD ["python", "bin/hello"]
