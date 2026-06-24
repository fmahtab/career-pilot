# Docker Setup Guide

This guide explains how to run CareerPilot inside a Docker container.

## Prerequisites

* Docker Desktop
* Docker Engine running

## 1. Build the Docker Image

From the project root:

```bash
docker build -t careerpilot .
```

## 2. Configure Environment Variables

Create a `.env` file in the project root.

If you are connecting the Docker container to PostgreSQL running on your Windows machine, use:

```env
DATABASE_URL=postgresql://postgres:your_password@host.docker.internal:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

`host.docker.internal` allows the Docker container to connect to services running on the host machine.

## 3. Run the Container

```bash
docker run -p 8000:8000 --env-file .env careerpilot
```

## 4. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Useful Commands

List running containers:

```bash
docker ps
```

Stop a container:

```bash
docker stop <container_id>
```

View logs:

```bash
docker logs <container_id>
```
