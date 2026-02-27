from sqlalchemy.orm import Session
from typing import List, Optional
from models.model import Category, Product, Comment, Users
from sqlalchemy import select
from schemas.schema import UserCreate
from auth.auth import get_password_hash



class CategoryRepo():
    def __init__(self, db:Session):
        self.db = db
        
    def get_all(self)->List[Category]:
        return self.db.query(Category).all()
    
class UserRepo():
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        stmt = select(Users).where(Users.id == user_id)
        
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_user_by_name(self,  user_name: str ):
        stmt = select(Users).where(Users.username == user_name)

        return self.db.execute(stmt).scalar_one_or_none()


    def create_user(self, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = Users(username = user.username,
                        email=user.email,
                        hashed_password=hashed_password
                        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
