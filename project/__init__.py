from flask import Flask
from flask_seasurf import SeaSurf


# Flask initialization
app = Flask(__name__)

# https://discussions.udacity.com/t/do-we-need-to-encrypt-the-state-when-implementing-csrf-protection/196609
csrf = SeaSurf(app)


# Import all routes
import project.handlers.oauth
import project.handlers.json_endpoints
import project.handlers.deletecategory
import project.handlers.deleteitem
import project.handlers.editcategory
import project.handlers.edititem
import project.handlers.newcategory
import project.handlers.newitem
import project.handlers.pagenotfound
import project.handlers.showall
import project.handlers.showitem
import project.handlers.showlogin
import project.handlers.singleitem