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
