# Reference:
# https://github.com/SteveWooding/fullstack-nanodegree-vm/blob/master/vagrant/catalog/catalog/connect_to_database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project import app as application
from project.db.database_setup import Base


def connect_to_database():
    """Connect to database and return a session object"""
    engine = create_engine('postgresql://catalog:password@localhost/catalog')
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session