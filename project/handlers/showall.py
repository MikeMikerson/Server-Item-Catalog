from flask import render_template
from flask import session as login_session
from sqlalchemy import asc

from project import app
from project.db.database_setup import Category
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in


@app.route('/')
@app.route('/category/')
def showAll():
    """
    Show all categories. This is the home page.
    """
    session = connect_to_database()
    categories = session.query(Category).order_by(asc(Category.name))
    session.close()
    return render_template('allcategories.html', categories=categories)
