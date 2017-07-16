from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# The database is created here.

class Questions(Base):
    __tablename__ = 'questions'

    index = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    OptionA = Column(String)
    OptionB = Column(String)
    OptionC = Column(String)
    OptionD = Column(String)



engine = create_engine('sqlite:///quidditch_questions.db')

Base.metadata.create_all(engine)
