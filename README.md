# CareerPilot

CareerPilot is an AI-powered job application management platform built with FastAPI and PostgreSQL. It helps job seekers organize applications, manage resumes, analyze job descriptions, and generate personalized cover letters using Generative AI.

The project demonstrates modern backend development practices including JWT authentication, REST APIs, PostgreSQL, Docker, resume parsing, and Claude AI integration.

## Features

### Authentication

- User registration
- Secure password hashing
- JWT-based authentication
- Protected API endpoints
- Current user profile endpoint

### Job Application Management

- Create, view, update, and delete job applications
- User-owned application access control

### Resume Management

- Upload PDF and DOCX resumes
- Secure filename sanitization
- Resume ownership protection
- Resume listing and retrieval
- Resume deletion

### Resume Intelligence

- Resume text extraction
- Parsed text storage in PostgreSQL
- Resume-to-job matching
- Matching skills identification
- Missing skills identification
- Match score calculation

### AI Features

- AI-powered cover letter generation using Claude
- Prompt-engineered cover letters tailored to uploaded resumes and job descriptions

### Developer Experience

- Docker support
- Docker Compose support
- Swagger/OpenAPI documentation
- Pytest test suite
- Environment-based configuration

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- PostgreSQL

### Authentication

- JWT
- OAuth2

### AI

- Anthropic Claude API
- Prompt Engineering

### File Processing

- PyPDF
- python-docx

### DevOps

- Docker
- Docker Compose

### Testing

- Pytest

## Architecture

CareerPilot follows a layered backend architecture.

```

Client ---> FastAPI Routers ---> Service Layer ---> Claude AI API ---> PostgreSQL

```

The AI service layer separates business logic from LLM interactions, making it easy to extend the application with additional AI features in the future.

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure:

* `your_password` matches your PostgreSQL password
* `job_tracker` matches your database name
* `your-secret-key` is replaced with a long random secret

> The `.env` file is excluded from Git and should never be committed.

---

## Running the Application

Choose one of the following approaches:

### Local Development

Run CareerPilot directly on your machine using Python, PostgreSQL, and a virtual environment.

➡️ [Local Setup Guide](docs/local-setup.md)

### Docker

Run CareerPilot inside a Docker container.

➡️ [Docker Setup Guide](docs/docker.md)

### Docker Compose (Recommended)

Run both the CareerPilot API and PostgreSQL database with a single command.

➡️ [Docker Compose Guide](docs/docker-compose.md)

---

## Running Tests

```bash
python -m pytest
```

---

## API Documentation

After starting the application, open the UI at:

```text
http://127.0.0.1:8000/docs
```

---

## Roadmap

### Completed

- FastAPI backend
- PostgreSQL integration
- JWT authentication
- Resume upload and parsing
- Resume-to-job matching
- AI-powered cover letter generation
- Docker support
- Docker Compose support
- Service layer architecture
- Claude API integration

### Planned

- AI resume improvement suggestions
- Interview question generation
- Job recommendation engine
- Email notifications
- Frontend dashboard

---

## Author

Fouzia Mahtab
