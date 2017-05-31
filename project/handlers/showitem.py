from flask import render_template
from flask import session as login_session

from project import app
from project.db.database_setup import Category, Item
from project.db.database_connect import connect_to_database
from project.handlers.decorators import category_exists
from project.utils.utils import getUserInfo


@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/item/')
@category_exists
def showItem(category_id):
    """
    Show all the items for the selected category.

    For the creator of the category, a button for editing and deleting
    the category is rendered.
    For the creator of an item, a button for editing and deleting the
    corresponding item is rendered.
    """
    session = connect_to_database()
    category = session.query(Category).filter_by(id=category_id).one()
    creator = getUserInfo(category.user_id)
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template(
        'item.html',
        items=items,
        category=category,
        creator=creator,
        login_session=login_session)
