# CareerPilot

CareerPilot is an AI-focused job application management platform built with FastAPI and PostgreSQL. It helps users track job applications, manage resumes, analyze job descriptions, and generate career-related insights.

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

## Environment Variables

Create a `.env` file in the project root and replace the placeholder values with your own local credentials:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure:

* `your_password` matches your local PostgreSQL password.
* `job_tracker` matches your database name.
* `your-secret-key` is replaced with a long random secret.

> Note: The `.env` file is excluded from Git and should never be committed to the repository.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/fmahtab/career-pilot.git
cd career-pilot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a PostgreSQL Database

Create a database named:

```text
job_tracker
```

### 6. Configure Environment Variables

Create the `.env` file using the example above.

### 7. Run the Application

```bash
uvicorn app.main:app --reload
```

### 8. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

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

### Planned

* AI-powered cover letter generation
* Improved matching engine
* Interview tracking
* Automated API testing
* Docker support
* Deployment

## Author

Fouzia Mahtab
