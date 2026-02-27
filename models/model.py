from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base
from datetime import datetime
from typing import List, Optional


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False,  index=True)
    description: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True, default=None) 
    products: Mapped[List["Product"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Category (id={self.id}, name='{self.name}')>"


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False,  index=True)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    image_url: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    category: Mapped["Category"] = relationship(back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price ={self.price})>"


class Comment(Base):
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    comment: Mapped[str] = mapped_column(nullable=False,  index=True)
    # xxx: Mapped[str] = mapped_column(nullable=False,  index=True)


    
class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False,  index=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
