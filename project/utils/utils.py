from project.db.database_setup import User
from project.db.database_connect import connect_to_database


def createUser(login_session):
    """
    Add a new user to the database
    """
    session = connect_to_database()
    newUser = User(
        name=login_session['username'],
        email=login_session['email'])
    session.add(newUser)
    session.commit()
    session.close()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    """
    Get all user information for the given ID
    """    
    session = connect_to_database()
    user = session.query(User).filter_by(id=user_id).one()
    session.close()
    return user


def getUserID(email):
    """
    Get the User ID for the given email if it exists
    """
    try:
        session = connect_to_database()
        user = session.query(User).filter_by(email=email).one()
        session.close()
        return user.id
    except:
        return None
