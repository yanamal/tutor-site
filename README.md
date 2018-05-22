# html-hax
This will be a web-based game where players learn about HTML by "hacking" web pages to solve puzzles.

Right now, this is just a small demo [App Engine](https://cloud.google.com/appengine/) app, using the [Flask](http://flask.pocoo.org/) library.

## Changes since release 0.1

### User Profile
The new file `user.py` defines a database format for storing app-specific information about our users.
In this example, we store the user's email (as defined by their Google login), and also a list of pages they've visited on our app.

The `get_by_user()` function in `user.py` retrieves the database entry for a give user, or creates a (blank) database entry if one doesn't already exist for this user.

We actually add data about the user in `main.py`, where we use the `before_request` handler to log what URL was requested before actually handling each request.

You can see the additional code for all of this in this commit: https://github.com/yanamal/html-hax-clean/commit/dfaa5cfb72ecb27dce4ec5383339b916b818f801
