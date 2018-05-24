# Use the NDB database structure that's integrated into App Engine.
from google.appengine.ext import ndb

from flask import Flask

app = Flask(__name__)

# TimestampedAction represets a timestamp/action/url triplet, used for for logging a user's interactions with the site.
class TimestampedAction(ndb.Model):
    timestamp = ndb.DateTimeProperty(auto_now_add=True) # timestamp. auto_now_add makes it so that the timestamp is automatically added when an instance is created.
    url = ndb.StringProperty() # the path/url associated with the action
    action = ndb.StringProperty() # the action taken (load, exit, focus, unfocus, click on button, ...)
    data = ndb.StringProperty() # additional data (e.g. which button was pressed)

# class representing User Profile data that's specific to this application:
class UserProfile(ndb.Model):
    user_email = ndb.StringProperty() # record the user's email, as specified by their Google log in. Just for simpler browsing.
    action_log = ndb.StructuredProperty(TimestampedAction, repeated=True)
    role = ndb.StringProperty() # user's role: student, TA, etc. TODO: maybe should be enum/int?

    # retrieve (or automatically create) user profile for the given App Engine user object.
    @classmethod
    def get_by_user(cls, user):
        profile = cls.get_by_id(user.user_id())
        # automatically create blank profile if user doesn't already exist
        if not profile:
            # TODO: use a whitelist of site-specific 'admin' users to automatically set role to 'admin' if email matches.
            profile = UserProfile(user_email = user.email(),
                                  action_log=[], role='student', id=user.user_id() )
            profile.put()
        return profile

    def log_action(self, url, action, data=None):
        self.action_log.append(TimestampedAction(url=url, action=action, data=data))
        self.put()

    def is_teacher(self):
        # TODO: probably better is_teacher logic.
        return not (self.role == 'student')
