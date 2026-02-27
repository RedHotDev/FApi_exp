from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class CategorySchm(BaseModel):
    id: int = Field(..., description='Category ID')
    name: str = Field(..., min_length=5, max_length=100,
                      description='Category Name')
    description: Optional[str] = None
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str = Field(..., min_length=5, max_length=100,
                          description='User Name')
    email: str = Field(..., min_length=5, max_length=100,
                       description='User Email')

class UserCreate(UserBase):
    password: str = Field(..., min_length=5, max_length=100,
                          description='User Password')
    

class User(UserBase):
    id: int = Field(..., description='User ID')
    is_active: bool = Field(..., description='User Status')
    class Config:   
        from_attributes = True
        
# Token schemas


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
