# syntax=docker/dockerfile:1

# Use a slim Python base image
FROM python:3.12-slim AS base

# Define environment variables
ENV POETRY_VERSION=1.8.5 \
    POETRY_CACHE_DIR=/root/.cache/pypoetry

# Install Poetry in a builder stage
FROM base AS builder
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install "poetry==${POETRY_VERSION}"

# Set working directory
WORKDIR /app

# Copy project files and install dependencies
COPY --link pyproject.toml .
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=${POETRY_CACHE_DIR} \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root --only main

# Final stage for the application
FROM base AS final

# Set working directory
WORKDIR /app

# Copy application files from builder stage
COPY --link --from=builder /app /app
COPY --link source.py test.py test_data.csv ./

# Create a non-root user
RUN groupadd appuser && useradd -g appuser -m appuser
USER appuser

# Set the default command
CMD ["python", "source.py"]