from sqlalchemy import Column, Integer, VARCHAR
from app.database.database import Base


class AlgemeneInformatie(Base):
    __tablename__ = "algemene_informatie"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(1024))
    organization = Column(VARCHAR(1024))
    department = Column(VARCHAR(1024))
    description_short = Column(VARCHAR(1024)) 
    type = Column(VARCHAR(1024))
    category = Column(VARCHAR(1024))
    website = Column(VARCHAR(1024))
    status = Column(VARCHAR(1024))
