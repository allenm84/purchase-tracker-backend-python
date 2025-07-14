from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, unique=True)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)