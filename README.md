# html-hax
This will be a web-based game where players learn about HTML by "hacking" web pages to solve puzzles.

Right now, this is just a minimal "Hello World" [App Engine](https://cloud.google.com/appengine/) app, using the [Flask](http://flask.pocoo.org/) library.

## App Structure
The two most important files are:

### app.yaml
This is where App Engine always starts. This file defines where each request should be routed.

In this version, all requests are routed to be handled by `main.py`. This version's handler also specifies that the user must log in before they are actually routed to the `main.py` script.

### main.py
This is a python script where we define how to handle certain requests. Right now, it only knows to handle the '/' request (which is just the main web page). It handles it by saying 'Hello, world.'

### Other files
#### .gitattributes and .gitignore
These are files that Git (the version control system) uses to decide how and what to add - or not add - to the repository when changes are made.

#### appengine_config.py
This is a standard (but optional) file for App Engine applications. In our case, we are only using it to put in a workaround to a bug that happens on Windows.

#### LICENSE
This is just a text file with the license for the code (this code is distributed under a permissive [MIT license](https://en.wikipedia.org/wiki/MIT_License)).

 You can actually use the GitHub interface to pick a license, and this fill will be automatically generated.

#### README.md
That's this file! It's a [Markdown](https://www.markdownguide.org/) file that GitHub automatically displays on the project's code page.
