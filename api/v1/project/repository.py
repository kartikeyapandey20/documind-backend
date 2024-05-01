from dotenv import load_dotenv
from fastapi import UploadFile , File,Depends
from sqlalchemy.orm import Session
from utils.file import FileUtils
from .model import Project
from core.deps import get_db
from .schema import ProjectCreate , CategoryIn
class ProjectRepository:
    def __init__(self):
        self.__file_utils = FileUtils()
    
    async def create_project(self, project_name : str,category_id :int,files: UploadFile = File(...),db : Session = Depends(get_db)) :
        file_name = self.__file_utils.upload_file(files)
        new_project = Project(
            project_name=project_name,
            document_url=file_name, 
            category_id=category_id )
        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return new_project
    
    def get_project(self, category_id : CategoryIn , db : Session = Depends(get_db)):

        project = db.query(Project).filter(Project.category_id == category_id.category_id).all()

        return project
            