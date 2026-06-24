# Docker Compose Guide

This guide explains how to run CareerPilot with Docker Compose.

Docker Compose is the recommended Docker-based setup because it starts both the FastAPI application and PostgreSQL database together.

## Prerequisites

* Docker Desktop
* Docker Compose

## 1. Configure Environment Variables

For Docker Compose, create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:testdb@db:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Important:

* `db` is the PostgreSQL service name inside `docker-compose.yml`.
* `testdb` should match `POSTGRES_PASSWORD` in `docker-compose.yml`.
* `job_tracker` should match `POSTGRES_DB` in `docker-compose.yml`.

## 2. Start the Application

```bash
docker compose up --build
```

This starts:

* `careerpilot_api`
* `careerpilot_db`

## 3. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## 4. Stop the Application

```bash
docker compose down
```

## 5. Stop and Remove Database Volume

Use this only when you want to reset the Docker database:

```bash
docker compose down -v
```

## Useful Commands

View running containers:

```bash
docker ps
```

View API logs:

```bash
docker logs careerpilot_api
```

View database logs:

```bash
docker logs careerpilot_db
```
