# syntax=docker/dockerfile:1

# Use a slim Python base image
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=2.1.1

# Install Poetry in the builder stage
FROM base AS builder
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install "poetry==${POETRY_VERSION}"

COPY ./app /app

# Set working directory
WORKDIR /app

# Copy project files
COPY --link pyproject.toml poetry.lock requirement.txt ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/root/.cache/poetry \
    poetry config virtualenvs.in-project true && \
    poetry install

# Final stage
FROM base AS final

# Set working directory
WORKDIR /app

# Copy application files from builder stage
COPY --link --from=builder /app /app

# Create a non-root user
RUN groupadd appuser && useradd -g appuser -m appuser
USER appuser

RUN python -m pip install -r requirement.txt
EXPOSE 5000
# Set entrypoint
ENTRYPOINT ["python", "main.py"]