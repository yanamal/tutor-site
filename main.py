#!/usr/bin/env python

# import libraries:
import os
import json
import random
from google.appengine.api import users
from flask import Flask,request,render_template

# Import code from our own files:
from user import UserProfile

# make the flask app:
app = Flask(__name__)

# Set up debug/error logging, when not running "for real" on Google App Engine:
if not os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
    app.debug = True  # with this setting on, the cause of Python errors is displayed in App Engine logs.

@app.route('/')
def hello():
    return render_template('hello.html', profile=UserProfile.get_by_user(users.get_current_user()))

@app.route('/select/<gamename>')
def select(gamename):
    return render_template('/selectGames/'+gamename+'.html', profile=UserProfile.get_by_user(users.get_current_user()))

# render a site-specific page from template
@app.route('/s/<page>')
def renderPage(page):
    return render_template('site-specific/'+page, profile=UserProfile.get_by_user(users.get_current_user()))

@app.route('/sort/<gamename>')
def renderSortGame(gamename):
    with app.open_resource('data/'+gamename+'.json') as f:
        sortData = json.load(f)
        categories = sortData.keys()
        terms = []
        for c in categories:
            terms.extend(sortData[c])
        random.shuffle(terms)
        return render_template('sortgame.html', categories=categories, terms=terms, gamename=gamename)

@app.route('/sortsubmit/<gamename>', methods=['POST'])
def renderSortResult(gamename):
    with app.open_resource('data/'+gamename+'.json') as f:
        answerData = json.load(f)
        totalTerms = 0;
        for category in answerData:
            totalTerms+= len(answerData[category])
        submittedData = request.form
        correct = 0
        wrong = 0
        for term in submittedData:
            category = submittedData[term]
            if term in answerData[category]:
                correct += 1
            else:
                wrong += 1
        return "correct: "+str(correct)+" wrong: "+str(wrong)+" omitted: "+str(totalTerms-correct-wrong)

# this special handler function will run for each request, regardless of the specific route, before the actual route handler
# in this example, we log each request in the user's profile, so that we have a histor of pages visited.
@app.before_request
def log_request():
    # get the user's profile entry from the database (or create one if this user is new to our database)
    profile = UserProfile.get_by_user(users.get_current_user())
    # log the visited URL (request.full_path) in the user's profile.
    profile.log_action(url=request.path, action="pageload")
