# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.0
FROM python:${PYTHON_VERSION} as builder

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001

RUN pip install poetry
COPY pyproject.toml poetry.lock ./

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --only-main


FROM python:${PYTHON_VERSION}-slim

WORKDIR /app
COPY --from=builder /app ./

EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000
