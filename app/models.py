from sqlalchemy import Column, Integer, String
from app.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)

    company = Column(String, nullable=False)

    position = Column(String, nullable=False)

    status = Column(String, nullable=False)

    user_id = Column(Integer, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)

    filename = Column(String, nullable=False)

    file_path = Column(String, nullable=False)
    
    user_id = Column(Integer, nullable=False)
