from flask import render_template
from flask import session as login_session
import random
import string

from project import app
from project.db.database_connect import connect_to_database


@app.route('/login')
def showLogin():
    """
    Renders the login page
    """
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)
