from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from database import get_db
from services.srv import CategorySrv
from schemas.schema import CategorySchm


routerCategory = APIRouter(prefix="/category", tags=["category"])

@routerCategory.get("/", response_model=List[CategorySchm])
def get_category(db: Session = Depends(get_db)):
    serv = CategorySrv(db)
    
    return serv.get_all_categories


