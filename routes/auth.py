from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from database import get_db
from schemas.schema import User, UserCreate, Token
from repository.repository import UserRepo
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth import authenticate_user, create_access_token,  get_current_active_user
from datetime import timedelta
from config import setting

routerAuth = APIRouter(prefix="/register", tags=["auth"])


@routerAuth.post("/", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepo(db)
    db_user = repo.get_user_by_name( user_name=user.username)
    print(db_user)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return repo.create_user(user=user)


@routerAuth.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=setting.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@routerAuth.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
