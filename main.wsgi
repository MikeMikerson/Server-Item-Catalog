"""
Main script used to start the application.
"""
import os.path
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/srv/catalog-app/Project-5-Item-Catalog')

from project import app as application
from flask import Flask
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.db.database_setup import Base
from project.db.database_seed import db_seed


# http://stackoverflow.com/questions/38523303/how-to-reload-a-flask-app-each-time-its-accessed/38524695#38524695
# This is used to refresh the server on template (html) changes
def before_request():
    application.jinja_env.cache = {}


application.before_request(before_request)
application.config['DATABASE_URL'] = 'postgresql://catalog:password@localhost/catalog'
application.secret_key = 'change_in_production'
db_seed()

