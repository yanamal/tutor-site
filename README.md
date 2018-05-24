# tutor-site
This is a generic structure for a web site with guided tutorials, built on [App Engine](https://cloud.google.com/appengine/) app, using the [Flask](http://flask.pocoo.org/) library.

It was mirrored from my own html-hax-clean repo, so some references to it may remain in old commits and releases.

It's currently mostly a set of templates with useful front-end features (expandable sections, pop-up dialogs) plus a backend which logs student actions.

All/most features are demoed in `templates/hello.html`

Current features:
- Require logging in via a Google account
- Expandable sections defined in HTML with the "accordion" class
- Pop-up dialog boxes defined in HTML with the "dialog" class
- Teacher-only sections (defined with a {% if%} jinja statement)
  - All new users are assumed to be of the "student" role; only non-students see the teacher-only content.
    - There is currently no in-app interface to change the role, have to edit the app's database
- Timestamped logging of user actions, including navigation to pages, opening/closing expandable content and dialogs.
  - There is also no in-app interface to view this, have to download or examine the app's database

Planned features:
- Log other client-side events, such as losing/gaining focus of a page, closing/navigating away from page, etc.
- Several types of review games/quizzes (and ability to add new instances by just adding a data file with the content), including:
  - Sort a set of terms into two categories
  - Select a part of a larger text which is most applicable to the current question/term
- Locking/unlocking content for specific users based on criteria like completion of other content, time (e.g. unlock for everyone at a certain point in the course)
- Some kind of definition of the sequence/flow/tree of pages that a student is meant to follow
- "Admin" interface for examining, changing, downloading database contents (logs, account roles)
