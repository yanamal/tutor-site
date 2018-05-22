# this whole file is for a workaround to a known (windows-only) bug between
# a Flask-related library (Click) and App Engine (https://github.com/pallets/click/issues/594)

# On Windows, Click tries to access and use a module called msvcrt,
# but it is not accessible in the App Engine environment.
# This workaround makes it so that Click doesn't realize it's on Windows (I think).

# When the app is actually deployed and running "in production", the bug doesn't matter
# since App Engine servers are not on Windows.

import os,sys

in_production = os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')
if (not in_production) and os.name == 'nt':
    os.name = None
    sys.platform = ''
