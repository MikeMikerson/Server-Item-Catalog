from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in, category_owner_check


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
@user_logged_in
@category_owner_check
def editCategory(category_id):
    """
    Allows the the creator of the category to edit the title and description.
    
    The button for to do this is only visible on the items page for
    the creator of the category.
    """
    session = connect_to_database()
    params = dict()
    has_error = False
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
        if request.form['description']:
            editedCategory.description = request.form['description']

        params['name'] = request.form['name']
        params['description'] = request.form['description']

        if not params['name']:
            params['error_name'] = "Please enter a name"
            has_error = True
        if not params['description']:
            params['error_description'] = "Please enter a description"
            has_error = True
        if has_error:
            session.close()
            return render_template(
                'editCategory.html',
                category=editedCategory,
                params=params)

        session.add(editedCategory)
        session.commit()
        flash('Category Successfully Edited %s' % editedCategory.name)
        session.close()
        return redirect(url_for('showAll'))
    else:
        return render_template(
            'editCategory.html',
            category=editedCategory,
            params=params)
