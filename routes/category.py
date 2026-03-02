from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from database import get_db
from services.srv import CategorySrv
from schemas.schema import CategorySchm
from auth.auth import get_current_user
from schemas.schema import User


routerCategory = APIRouter(prefix="/category", tags=["category"])

@routerCategory.get("/", response_model=List[CategorySchm])



@routerCategory.get("/", response_model=List[CategorySchm])
def get_category(db: Session = Depends(get_db)):
    srv = CategorySrv(db)
    
    return srv.get_all_categories()


@routerCategory.get("/protected", response_model=List[CategorySchm])
def get_category(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    print(user.username)
    srv = CategorySrv(db)
    
    return srv.get_all_categories()
