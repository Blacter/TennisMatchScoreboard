from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text

from model.base import Base
from model.match import Match
from model.player import Player
from config import settings


engine = create_engine(
    url = settings.DATABASE_URL_pymysql,
    echo = True
)

def create_database() -> None:    
    Base.metadata.create_all(engine)    
        
print('trace: 0')
create_database()
    
