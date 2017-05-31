from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category, Item
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in


@app.route('/category/<int:category_id>/item/new/', methods=['GET', 'POST'])
@user_logged_in
def newItem(category_id):
    """
    Create a new item. The name, description and price must be filled
    in order to process the request.
    """
    session = connect_to_database()
    params = dict()
    has_error = False
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = Item(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            category_id=category_id,
            user_id=login_session['user_id'])
        params['name'] = newItem.name
        params['description'] = newItem.description
        params['price'] = newItem.price

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
                'newitem.html',
                category_id=category_id,
                params=params)

        session.add(newItem)
        session.commit()
        flash('New Item %s Item Successfully Created' % (newItem.name))
        session.close()
        return redirect(url_for('showItem', category_id=category_id))
    else:
        return render_template(
            'newitem.html',
            category_id=category_id,
            params=params)
