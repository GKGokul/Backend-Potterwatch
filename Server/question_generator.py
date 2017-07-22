from random import randint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from flask import Flask, jsonify

import json

from question_database import Base, Questions

app = Flask(__name__)

engine = create_engine('sqlite:///quidditch_questions.db', connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

array = []


# Generating a random number
def generatenumber():
    while len(array) < 10:
        randomNumber = (randint(1, 10))
        if ((randomNumber in array) or randomNumber == None):
            generatenumber()
        else:
            array.append(randomNumber)


def TheFunction():
    generatenumber()
    value = []
    b = array[:]
    del array[:]
    k = 0
    for i in b:
        result = session.query(Questions).filter_by(index=i).one()
        value.append(result)



    jsondata = {"Questions": []}

    question = []
    for i in value:
        name = "question"+str(i.index)
        question.append({name: {"question": str(i.question), "optionA": str(i.OptionA), "optionB": str(i.OptionB), "optionC": str(i.OptionC), "optionD": str(i.OptionD), "answer": str(i.answer)}})


    #jsondata[0].append(question)
    jsonStr = json.dumps(question)
    print(jsonStr)
    return jsonStr


TheFunction()
