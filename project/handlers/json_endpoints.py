from flask import jsonify
from project.db.database_setup import Category, Item
from project.db.database_connect import connect_to_database
from project.handlers.decorators import category_exists, item_exists

from project import app
import json


@app.route('/category/<int:category_id>/item/JSON')
@category_exists
def categoryJSON(category_id):
    """
    Show the JSON for the items of a category
    """
    session = connect_to_database()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    session.close()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
@item_exists
def itemJSON(category_id, item_id):
    """
    Show the JSON for any given item
    """
    session = connect_to_database()
    item = session.query(Item).filter_by(id=item_id).one()
    session.close()
    return jsonify(item=item.serialize)


@app.route('/category/JSON')
def categoriesJSON():
    """
    Show the JSON for all categories
    """
    session = connect_to_database()
    categories = session.query(Category).all()
    session.close()
    return jsonify(categories=[c.serialize for c in categories])
