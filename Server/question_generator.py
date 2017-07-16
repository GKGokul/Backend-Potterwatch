from random import randint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from user_database import Base

engine = create_engine('sqlite:///quidditch_questions.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


array=[]
# Generating a random number
def generatenumber():
    while len(array) < 7:
        randomNumber = (randint(1, 7))
        if (randomNumber in array):
            generatenumber()
        else:
            array.append(randomNumber)
            return randomNumber


randomnumber = generatenumber()


