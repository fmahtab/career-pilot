from app.database import SessionLocal

db = SessionLocal()

print("Database session opened successfully")

db.close()

print("Database session closed")