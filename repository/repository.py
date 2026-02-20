from sqlalchemy.orm import Session
from typing import List, Optional
from models.model import Category, Product
# from schemas.category import CategoryCreate


class CategoryRepo():
    def __init__(self, db:Session):
        self.db = db
        
    def get_all(self)->List[Category]:
        return self.db.query(Category).all()