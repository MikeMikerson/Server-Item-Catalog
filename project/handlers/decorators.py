from flask import render_template, redirect, url_for, flash
from flask import session as login_session

from functools import wraps
from project.db.database_setup import Category, Item, User
from project.db.database_connect import connect_to_database

from project import app
from project.utils.utils import getUserInfo


# Check if owner of category
def category_owner_check(function):
    """
    Checks if the person logged in is the owner of the category
    """
    @wraps(function)
    def wrapper(category_id):
        session = connect_to_database()
        category = session.query(Category).filter_by(id=category_id).one()
        creator = getUserInfo(category.user_id)
        session.close()
        if creator.id != login_session['user_id']:
            flash('Sorry, but you did not create this category')
            return redirect(url_for('showAll'))
        else:
            return function(category_id)
    return wrapper


# Check if owner of item
def item_owner_check(function):
    """
    Checks if the person logged in is the owner of a particular item
    """
    @wraps(function)
    def wrapper(category_id, item_id):
        session = connect_to_database()
        item = session.query(Item).filter_by(id=item_id).one()
        creator = getUserInfo(item.user_id)
        session.close()
        if creator.id != login_session['user_id']:
            flash('Sorry, but you did not create this item')
            return redirect(url_for('showAll'))
        else:
            return function(category_id, item_id)
    return wrapper


# Check if category exists
def category_exists(function):
    """
    Checks if the category exists and renders the home page if it does not
    """
    @wraps(function)
    def wrapper(category_id):
        session = connect_to_database()
        category = session.query(Category).filter_by(id=category_id).first()
        session.close()
        if not category:
            flash('Sorrry, but that category does not exist')
            return redirect(url_for('showAll'))
        else:
            return function(category_id)
    return wrapper


# Check if item exists
def item_exists(function):
    """
    Checks if the category and the item exists.
    
    Also checks if the item belongs to the category if they both exist
    """
    @wraps(function)
    def wrapper(category_id, item_id):
        session = connect_to_database()
        category = session.query(Category).filter_by(id=category_id).first()
        item = session.query(Item).filter_by(id=item_id).first()
        if not category:
            flash("Sorry, but that category does not exist")
            return redirect(url_for('showAll'))
        if not item:
            flash("Sorry, but that item doesn't exist")
            return redirect(url_for('showAll'))
        if category.id != item.category.id:
            flash("Sorry, but that item doesn't exist for that category")
            return redirect(url_for('showAll'))
        else:
            return function(category_id, item_id)
    return wrapper


# Check if user logged in
def user_logged_in(function):
    """
    Redirects to the login page if the user is not logged in
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('showLogin'))
        else:
            return function(*args, **kwargs)
    return wrapper
