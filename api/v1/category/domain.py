from .repository import CategoryRepository


class CategoryDomain():
    def __init__(self):
        self.__repository  = CategoryRepository()
        
    def create(self, category , db):
        return self.__repository.create(category , db)
    
    def get_categories(self, db):
        return self.__repository.get_categories(db)