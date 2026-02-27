from config import setting
from database import get_db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from models.model import Users
from database import SessionLocal
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.schema import Token, TokenData, User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def veryfi_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(db:Session, username: str, password: str):
    stmt = select(Users).where(Users.username ==  username)
    user = db.execute(stmt).scalar_one_or_none()
    
    if not user or not veryfi_password(password, user.hashed_password):
        return False
    return user
   
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode, setting.secret_key, algorithm=setting.algorithm)
    return encode_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db:Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    stmt = select(Users).where(Users.username == username)
    user = db.execute(stmt).scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
