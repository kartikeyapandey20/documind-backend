from pydantic import BaseModel
from datetime import datetime

class CategorySchema(BaseModel):
    category_name: str
    
class CategoryOutSchema(BaseModel):
    id: int
    category_name: str
    created_at: datetime