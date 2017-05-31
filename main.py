"""
Main script used to start the application.
"""
import os.path

from project import app
from flask import Flask
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.db.database_setup import Base, catalog_create
from project.db.database_seed import db_seed


# http://stackoverflow.com/questions/38523303/how-to-reload-a-flask-app-each-time-its-accessed/38524695#38524695
# This is used to refresh the server on template (html) changes
def before_request():
    app.jinja_env.cache = {}


if __name__ == '__main__':
    app.before_request(before_request)
    app.config['DATABASE_URL'] = 'sqlite:///itemcatalog.db'
    app.secret_key = 'change_in_production'

    if app.config['DATABASE_URL'] == 'sqlite:///itemcatalog.db':
        if os.path.isfile('itemcatalog.db') is False:
            catalog_create(app.config['DATABASE_URL'])
            db_seed()

    app.debug = True
    app.run(host='0.0.0.0', port=8080)
