'''
from permutation_database import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from oauth2client import client
from flask import Flask, jsonify, request, url_for, abort, g, redirect
import httplib2
import json
import itertools

engine = create_engine('sqlite:///permutations.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
'''

import itertools

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = set(itertools.permutations(list))
print answer
