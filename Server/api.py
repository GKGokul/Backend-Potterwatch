import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import httplib2
from flask import Flask, request

import question_generator
from user_database import Base, User

app = Flask(__name__)

engine = create_engine('sqlite:///userinfo.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

appid = '115224489100238'
appsecret = '108dd482d07cfa16df57e659fb6b92b3'


# This is just the home of the Server
@app.route('/')
def home():
    print 'HOME of the Server'
    return 'HOME of the Server'


# This is the decorator for interacting with Facebook API
@app.route('/fbconnect', methods=['POST', 'GET'])
def fbconnect():
    print request
    name = request.json.get("name")
    id = request.json.get("id")
    email = request.json.get("email")
    gender = request.json.get("gender")
    auth_token = request.json.get("auth_token")

    print name
    print id
    print email
    print gender
    print auth_token

    url = (
        'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=fb_exchange_token&fb_exchange_token=%s' % (
            appid, appsecret, auth_token))

    h = httplib2.Http()
    header, result = h.request(url, 'GET')
    token = json.loads(result)['access_token']
    UserEntry = User(userid=id, displayname=name, emailid=email, photouri="", gender=gender, accesstoken=token)
    session.add(UserEntry)
    session.commit()

    return 'SUCCESS'


array = []


# This is the decorator for the retrival of question for quidditch
@app.route('/questions', methods=['GET'])
def giveQuestion():
    value = question_generator.TheFunction()
    print(value)


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.43.232', port=8080)
