from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from user_database import Base

engine = create_engine('sqlite:///quidditch_questions.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

