from fastapi import Depends, HTTPException, status
from api.v1.category.model import Category
from .schema import CategorySchema
from core.deps import get_db

class CategoryRepository:
    
    def create(self, category: CategorySchema):
        category_db = self.db.query(Category).filter(Category.name == category.name).first()
        if category_db:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Category already exists")
        category_db = Category(name=category.name, user_id=user.get('id'))
        self.db.add(category_db)