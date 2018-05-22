# tutor-site
This will be a generic structure for a web site with guided tutorials.

Right now, this is just a small demo [App Engine](https://cloud.google.com/appengine/) app, using the [Flask](http://flask.pocoo.org/) library.

It was mirrored from my own html-hax-clean repo, so some references to it may remain in old commits and releases.

Planned features:
- Automatic logging of a user's navigation and interaction history, with timestamps
- Ability to add parts of the page only be visible to admin/teacher role users
- Ability to add "modal" content that pops up when the user presses a button/link (definitions, rubrics, etc.) (that also log when a user has clicked on them)
- Several types of review games/quizzes (and ability to add new instances by just adding a data file with the content), including:
  - Sort a set of terms into two categories
  - Select a part of a larger text which is most applicable to the current question/term
- Locking/unlocking content for specific users based on criteria like completion of other content, time (e.g. unlock for everyone at a certain point in the course)
