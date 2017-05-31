from flask import render_template
from project import app


@app.errorhandler(500)
def page_not_found(er):
    """
    Render errors.html when there's a 500 error
    """
    return render_template('errors.html'), 500


@app.errorhandler(404)
def page_not_found(er):
    """
    Render errors.html when there's a 404 error
    """
    return render_template('errors.html'), 404


@app.errorhandler(400)
def page_not_found(er):
    """
    Render errors.html when there's a 400 error
    """    
    return render_template('errors.html'), 400
