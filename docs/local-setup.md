# Local Setup Guide

This guide explains how to run CareerPilot directly on your local machine using Python, PostgreSQL, and Uvicorn.

## Prerequisites

* Python 3.13+
* PostgreSQL
* Git

## 1. Clone the Repository

```bash
git clone https://github.com/fmahtab/career-pilot.git
cd career-pilot
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

## 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Create the PostgreSQL Database

Create a database named:

```text
job_tracker
```

## 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/job_tracker
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace the placeholder values with your local PostgreSQL credentials.

## 7. Run the Application

```bash
uvicorn app.main:app --reload
```

## 8. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```
