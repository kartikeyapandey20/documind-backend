from .domain import CategoryDomain
from fastapi import APIRouter ,status ,Depends
from .schema import CategorySchema , CategoryOutSchema
from sqlalchemy.orm import Session
from core.deps import get_db
class CategoryRouter:
    def __init__(self)->None:
        self.__domain = CategoryDomain()
        
    @property
    def router(self):
        api_router = APIRouter(prefix="/category",tags=["category"])
        
        @api_router.post("/",status_code=status.HTTP_201_CREATED ,response_model=CategoryOutSchema)
        def create_category(category: CategorySchema, db : Session = Depends(get_db)):
            return self.__domain.create(category, db)
        
        @api_router.get("/", response_model=list[CategoryOutSchema])
        def get_categories(db : Session = Depends(get_db)):
            return self.__domain.get_categories(db)
        
        return api_router