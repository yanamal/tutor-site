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

### HTML pages
Instead of just returning the text "Hello, world", our app now serves two types of HTML files!

#### templated
The root of the webpage `'\'` is still being rendered by main.py, but this time, we are using a templated html file, `templates/hello.html`.

All templated files must live in the `templates` directory, because that's where Flask looks for them (though technically there's probably a way to override that).

The benefit of rendering a templated file through a python handler is that we can add in information from the server, such as the user's nickname! In this example, we get the nickname by using `users.get_current_user().nickname()`, pass it in as `name`, and that means that wherever it says `{{ name }}` in `templates/hello.html`, the actual nickname will be used.

The commit that adds templated HTML is here: https://github.com/yanamal/html-hax-clean/commit/9d97e931920cc39d5d122ee1f6f5bf9b3f5c6f09

#### static
A static file is just a plain simple HTML (or CSS, or JavaScript, or image) file that doesn't get processed by the server. It's a simple way of just serving some content without applying any custom processing logic.

*Note:* That means that visit-tracking also doesn't apply to the static files, since it's part of the python logic. So for simple files that need tracking, we may still want to use a template, just without parameters.

The commit that adds static HTML is here:
https://github.com/yanamal/html-hax-clean/commit/a627a481aa6fd9cd43a6885221f7bae1986ce729
