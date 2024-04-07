from db.database import Base
from sqlalchemy import Column , String , Integer , Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Category(Base):
    
    __tablename__ = 'category'
     
    id = Column(Integer, primary_key=True, nullable=False)
    category_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))