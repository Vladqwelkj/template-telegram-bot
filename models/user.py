from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)

    habits = relationship('Habit')
