from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.database import get_db
from app.models import User
from app.schemas import UserCreate
from app.schemas import UserLogin

router = APIRouter()

password_hash = PasswordHash.recommended()

SECRET_KEY = "temporary-secret-key-change-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            return {
                "error": "Invalid token"
            }
        
    except JWTError:
        return {
            "error": "Invalid token"
        }
    
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user is None:
        return {
            "error": "User not found"
        }
    
    return user



def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# Register a new user account
@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )
    
    if existing_user:
        return{"error": "Email already registered"}
    
    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "email": new_user.email
        }
    }


# Login and return a JWT access token
@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
    ):
    existing_user = (
        db.query(User)
        .filter(User.email == form_data.username)
        .first()
    )

    if not existing_user:
        return {
            "error": "Invalid email or password"
        }
    
    if not verify_password(form_data.password, existing_user.hashed_password):
        return {
            "error": "Invalid email or password"
        }

    access_token = create_access_token(
        data={"sub": existing_user.email, "user_id": existing_user.id}
    )

    return{
        "access_token": access_token,
        "token_type": "bearer"
    }

