from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in


@app.route('/category/new/', methods=['GET', 'POST'])
@user_logged_in
def newCategory():
    """
    Create a new category. The name and description must be filled
    in order to process the request.
    """    
    session = connect_to_database()
    params = dict()
    has_error = False
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'],
            description=request.form['description'],
            user_id=login_session['user_id'])
        params['name'] = newCategory.name
        params['description'] = newCategory.description

        if not params['name']:
            params['error_name'] = "Please enter a name"
            has_error = True
        if not params['description']:
            params['error_description'] = "Please enter a description"
            has_error = True
        if has_error:
            session.close()
            return render_template('newCategory.html', params=params)

        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        session.close()
        return redirect(url_for('showAll'))
    else:
        return render_template('newCategory.html', params=params)
