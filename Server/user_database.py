from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


# The database is created here.

class User(Base):
    __tablename__ = 'user'

    userid = Column(Integer, primary_key=True)
    displayname = Column(String, nullable=False)
    emailid = Column(String)
    photouri = Column(String)
    gender = Column(String)
    accesstoken = Column(String)



engine = create_engine('sqlite:///userinfo.db')

Base.metadata.create_all(engine)
