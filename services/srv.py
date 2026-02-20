from sqlalchemy.orm import Session
from typing import List
from repository.repository import CategoryRepo
from schemas.schema import CategorySchm
from fastapi import HTTPException, status


class CategorySrv:
    def __init__(self, db: Session):
        self.repository = CategoryRepo(db)

    def get_all_categories(self) -> List[CategorySchm]:
        category = self.repository.get_all()
        return [CategorySchm.model_validate(cat) for cat in category]

 
