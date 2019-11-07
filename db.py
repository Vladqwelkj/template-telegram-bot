from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from config import Config

engine = create_engine(Config.DB_URL)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


# noinspection PyUnresolvedReferences
def init_db():
    from models import User, Habit
    Base.metadata.create_all(bind=engine)
