# CareerPilot

CareerPilot is a job application management platform built with FastAPI and PostgreSQL. It helps users track job applications, manage resumes, match resumes against job descriptions, and generate tailored cover letters.

## Features

### Authentication

* User registration
* Secure password hashing
* JWT-based authentication
* Protected API endpoints
* Current user profile endpoint

### Job Application Management

* Create applications
* View applications
* Update applications
* Delete applications
* User-owned application access control

### Resume Management

* Upload PDF and DOCX resumes
* Resume file validation
* Secure filename sanitization
* Resume ownership protection
* Resume listing and retrieval
* Resume deletion

### Resume Intelligence

* Resume text extraction from PDF and DOCX files
* Parsed text storage in PostgreSQL
* Resume-to-job matching
* Matching skills identification
* Missing skills identification
* Match score calculation

### Cover Letter Generation

* Generate tailored cover letters using application and resume data

## Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* python-docx
* PyPDF
* python-dotenv
* pytest
* Docker
* Docker Compose

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

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

---

## Roadmap

### Completed

* FastAPI project setup
* PostgreSQL integration
* SQLAlchemy models
* User authentication
* JWT authorization
* User-owned applications
* Resume upload and parsing
* Resume text persistence
* Resume-to-job matching
* Cover letter generation
* Upload validation
* Environment variable configuration
* Automated API testing
* Docker support
* Docker Compose support

### Planned

* AI-powered cover letter generation
* Improved matching engine
* Interview tracking
* Deployment

---

## Author

Fouzia Mahtab
