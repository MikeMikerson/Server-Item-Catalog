from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category, Item
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in, item_exists
from project.utils.utils import getUserInfo


@app.route('/category/<int:category_id>/item/<int:item_id>/')
@item_exists
def singleItem(category_id, item_id):
    """
    Renders the page for a single item.

    Buttons for editing and deleting the item are also rendered for the
    item creator
    """
    session = connect_to_database()
    item = session.query(Item).filter_by(id=item_id).one()
    creator = getUserInfo(item.user_id)
    category = session.query(Category).filter_by(id=category_id).one()
    return render_template(
        'singleitem.html',
        category=category,
        item=item,
        creator=creator,
        login_session=login_session)
