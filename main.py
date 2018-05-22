#!/usr/bin/env python

# import libraries:
import os
from google.appengine.api import users
from flask import Flask,request

# Import code from our own files:
from user import UserProfile

# make the flask app:
app = Flask(__name__)

# Set up debug/error logging, when not running "for real" on Google App Engine:
if not os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
    app.debug = True  # with this setting on, the cause of Python errors is displayed in App Engine logs.

@app.route('/')
def hello():
    return 'Hello World!'

# this special handler function will run for each request, regardless of the specific route, before the actual route handler
# in this example, we log each request in the user's profile, so that we have a histor of pages visited.
@app.before_request
def log_request():
    # get the user's profile entry from the database (or create one if this user is new to our database)
    profile = UserProfile.get_by_user(users.get_current_user())

    #Take the current page (request.full_path) and append it to the list of visited_pages that we keep in UserProfile.
    profile.visited_pages.append(request.full_path)

    # write the changes to the database (without profile.put() the changes don't take effect)
    profile.put()
