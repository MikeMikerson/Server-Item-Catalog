from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from project import app
from project.db.database_setup import Category
from project.db.database_connect import connect_to_database
from project.handlers.decorators import user_logged_in, category_owner_check


@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
@user_logged_in
@category_owner_check
def deleteCategory(category_id):
    """
    Deletes the category and all the items that belong to it from the database
    """
    session = connect_to_database()
    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    session.close()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showAll', category_id=category_id))
    else:
        return render_template(
            'deleteCategory.html',
            category=categoryToDelete)
