from fastapi import Depends, HTTPException, status
from api.v1.category.model import Category
from .schema import CategorySchema
from core.deps import get_db
from sqlalchemy.orm import Session

class CategoryRepository:
    
    def create(self,category: CategorySchema , db : Session = Depends(get_db)):
        
        new_category = Category(**category.dict())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        
        return new_category
    
    def get_categories(self,db : Session = Depends(get_db)):
        category =  db.query(Category).all()

        return category