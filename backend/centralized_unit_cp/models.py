from sqlalchemy import Column, Integer, String
from database import Base

class Connection(Base):
    __tablename__ = 'connections'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
