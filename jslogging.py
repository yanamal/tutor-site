from google.appengine.api import users
from flask import Flask,request,render_template

# Import code from our own files:
from user import UserProfile

# make the flask app:
app = Flask(__name__)

# This special "logging" handler will log whatever the JS side asks it to.
# Technically not the most tamper-proof, but only using it to log JS events.
# the reason it's in a separate handler is because all requests that go through main.py
# themselves get logged as a user action, which is unnecessary for automated "logging" requests.
@app.route('/logevent', methods=['POST'])
def logEvent():
    profile = UserProfile.get_by_user(users.get_current_user())
    profile.log_action( url=request.form["path"],
                        action=request.form["action"],
                        data=request.form["data"])
    return "logged"
