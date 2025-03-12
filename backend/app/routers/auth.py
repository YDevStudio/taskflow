from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import timedelta

from app import models, schemas
from app.database import get_db
from app.config import settings
from app.utils import hash_password, verify_password, create_access_token

router = APIRouter()

# Register
@router.post("/register", response_model=schemas.UserOut)
def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if username or email exists
    user_by_username = db.query(models.User).filter(models.User.username == user_data.username).first()
    user_by_email = db.query(models.User).filter(models.User.email == user_data.email).first()

    if user_by_username or user_by_email:
        raise HTTPException(status_code=400, detail="Username or email is already taken.")

    hashed_pwd = hash_password(user_data.password)
    new_user = models.User(username=user_data.username, email=user_data.email, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Login
@router.post("/login", response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    if not user:
        # 🔴 Return 404 if email does not exist
        raise HTTPException(status_code=404, detail="No account found with this email.")

    if not verify_password(user_credentials.password, user.hashed_password):
        # 🔴 Return 403 if password is incorrect
        raise HTTPException(status_code=403, detail="Incorrect password. Please try again.")

    access_token_expires = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    access_token = create_access_token(
        data={"user_id": str(user.id)},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer", "username": user.username}
# Utility to get current user from token
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise credentials_exception

    return user