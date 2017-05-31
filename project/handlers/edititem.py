from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category, Item
from project.db.database_connect import connect_to_database
from project.handlers.decorators import (
    user_logged_in,
    item_owner_check,
    item_exists)


@app.route(
    '/category/<int:category_id>/item/<int:item_id>/edit',
    methods=['GET', 'POST'])
@item_exists
@user_logged_in
@item_owner_check
def editItem(category_id, item_id):
    """
    Allows the creator of an item to delete it from the database
    """
    session = connect_to_database()
    params = dict()
    has_error = False
    editedItem = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']

        params['name'] = request.form['name']
        params['description'] = request.form['description']
        params['price'] = request.form['price']

        if not params['name']:
            params['error_name'] = "Please enter a name"
            has_error = True
        if not params['description']:
            params['error_description'] = "Please enter a description"
            has_error = True
        if not params['price']:
            params['error_price'] = "Please enter a price"
            has_error = True
        if has_error:
            session.close()
            return render_template(
                'edititem.html',
                category_id=category_id,
                item_id=item_id,
                item=editedItem,
                params=params)

        session.add(editedItem)
        session.commit()
        session.close()
        flash('Item Successfully Edited')
        return redirect(url_for('showItem', category_id=category_id))
    else:
        return render_template(
            'edititem.html',
            category_id=category_id,
            item_id=item_id,
            item=editedItem,
            params=params)
