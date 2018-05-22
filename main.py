#!/usr/bin/env python

# import libraries and other code:
import os
from flask import Flask

# make the flask app:
app = Flask(__name__)

# Set up debug/error logging, when not running "for real" on Google App Engine:
if not os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
    app.debug = True  # with this setting on, the cause of Python errors is displayed in App Engine logs.

@app.route('/')
def hello():
    return 'Hello World!'
