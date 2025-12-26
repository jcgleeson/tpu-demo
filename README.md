# hello (Docker-enabled)

A minimal Python "hello world" package with Docker support.

Quick start (build & run):

Build the Docker image:

```bash
# from project root (/Users/jamesgleeson/code/tpu)
docker build -t hello:latest .
```

Run the CLI in a container:

```bash
docker run --rm hello:latest
docker run --rm hello:latest Alice
```

Or using docker-compose:

```bash
docker-compose up --build
# then from another terminal:
# docker-compose run --rm hello python bin/hello Bob
```

Run tests inside the container (recommended to run locally):

```bash
# Build the image (if not already built)
docker build -t hello:latest .

# Run pytest inside the container
docker run --rm hello:latest pytest -q
```

Local non-Docker usage

```bash
python -m pip install -e .[dev]
pytest -q
```

