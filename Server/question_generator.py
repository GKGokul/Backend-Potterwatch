# This file generates a list of questions in a random order and returns the data in JSON format.
from random import randint
from question_database import Base, Questions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, jsonify

import json

app = Flask(__name__)

# To make the session accesible globally.
engine = create_engine('sqlite:///quidditch_questions.db', connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

array = []

# Generating a random number and adding to the array
def generatenumber():
    while len(array) < 20:
        randomNumber = (randint(1, 20))
        if ((randomNumber in array) or randomNumber == None):
            generatenumber()
        else:
            array.append(randomNumber)

# This function is used in the API call
def TheFunction():
    generatenumber()
    value = []
    b = array[:]
    del array[:]

    for i in b:
        result = session.query(Questions).filter_by(index=i).one()
        value.append(result)

    question = []
    for i in value:
        name = "questions"
        question.append({name: {"question": str(i.question), "optionA": str(i.OptionA), "optionB": str(i.OptionB),
                                "optionC": str(i.OptionC), "optionD": str(i.OptionD), "answer": str(i.answer)}})

    jsonStr = json.dumps(question)
    return jsonStr